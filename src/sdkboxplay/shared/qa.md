## Q&A

### How To Submit Float Score

```c++
static void submitScore( const std::string& leaderboard_name, long score );
```

The meaning of the score value depends on the formatting of the leaderboard established in the developer console.

Fixed-point formats:

score represents a raw value, and will be formatted based on the number of decimal places configured. A score of 1000 would be formatted as 1000, 100.0, or 10.00 for 0, 1, or 2 decimal places.

eg. if you want to submit score 3.14, you must set score formats is `Fixed Point To 2 Decimal` (change score format at apple/google develope website), and invoke like follow:

```c++
submitScore("leaderboardName", 3.14 * 100);

```

