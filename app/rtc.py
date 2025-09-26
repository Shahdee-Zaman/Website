import redis
from datetime import datetime, timezone


"""
    RTC(Redis Token Counter) uses Redis to track of token usage.
    RTCLimit stop further calls from being made when the tier limit is reached, allowing anyone to avoid incurring extra charges.
    Automatically check for Daily Reset using UTC timezone before every call.
"""
# ----------------- Start Of Class Creation -----------------

class RTCLimit:

    def __init__(self, host, port, limit, db=0):
        # Redis setup
        self.database = redis.Redis(host, port, db)
        # Setting TPD Usage Limit. Leaving Extra space for outputs.
        self.Gemini_TPD_limit = limit - 50000

    # Check for Daily TPD reset
    def check_daily_reset(self):
        current_date = datetime.now(timezone.utc).strftime('%y:%m:%d')
        # Decode the date to compare with current_date
        if str(self.redis_decoder('date')) != current_date:
            self.database.set('date', current_date)
            self.database.set('token_usage', 0)


    # Check if the prompt is within the Daily Token limit
    def has_tokens(self, tokens):
        estimated_total = int(self.redis_decoder('token_usage')) + tokens
        # The Resulting token will exceed TPD usage limit
        if estimated_total <= self.Gemini_TPD_limit:
            self.database.incrby('token_usage', tokens)
            return True
        return False

# ----------------- End Of Class Creation -----------------

    # ----------------- Helper Functions -----------------

    # Returns the number of tokens used
    def tokens_used(self):
        self.check_daily_reset()
        if self.redis_decoder('token_usage'):
            return int(self.redis_decoder('token_usage'))
        # Return 0 if no token was called since Redis initialization
        else:
            return 0

    # Decode returned values from bytes
    def redis_decoder(self, value):
        decoded = self.database.get(value)
        return decoded.decode() if decoded else None


    # Decode returned values from bytes
    def redis_decoder(self, value):
        decoded = self.database.get(value)
        return decoded.decode() if decoded else None

    # ----------------- End of Helper Functions -----------------

    # ----------------- Main Function -----------------

    ## The required function that needs to be called to properly run the Class

    # Returns True if the api call can proceed
    def generate(self, tokens):
        self.check_daily_reset()
        if self.has_tokens(tokens):
            return True
        return False

    # Increments the token count of response
    def response_count(self, token):
        self.database.incrby('token_usage', token)

