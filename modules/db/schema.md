# Database Layout

## algorithms
#### Just a table for algorithm references
- Algorithm Name
- Agressiveness

## userData
#### Store information about end users
- email (string)
- Name (string)
- ...

## cryptoData
#### Stores Current Market State
- CoinID (string)
- ExchangeID (string)
- Value (in $/coin)
- Timestamp

## tradingPools
#### Keeps track of trading pools values and coin associations
- AlgorithmID (Foreign Key in Algorithm Table)
- Aggressiveness (Score of 0-1)
- Value (Total Value in $)

## tradingPoolCoinData
#### Keeps Track of Coin and USD amounts associated with each pool
- TradingPoolID (Foreign Key in TradingPools Table)
- CoinID (string)
- CoinAmount (Number of coins held in that pool)

## tradingPoolUserData
#### Stores User Investment Data
- UserID (Foreign Key in Users Table)
- TradingPoolID (Foreign Key in TradingPools Table)
- Amount (Percentage of pool owned)

## trades
#### Stores information about caluculated and executed trades
- TradingPoolID (Foreign Key in TradingPools Table)
- CoinFrom (string)
- CoinTo (string)
- Amt (In $)
- ExchangeID (string)
- Completed (bit is 1 if completed)
