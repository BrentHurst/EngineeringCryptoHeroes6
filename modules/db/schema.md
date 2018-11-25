# Database Layout

## algorithms
#### Just a table for algorithm references
- ID (generated)
- Algorithm Name
- Agressiveness

## userData
#### Store information about end users
- ID (generated)
- email (string)
- Name (string)
- ...

## cryptoData
#### Stores Current Market State
- ID (generated)
- CoinID (string)
- ExchangeID (string)
- Value (in $/coin)
- Timestamp

## tradingPools
#### Keeps track of trading pools values and coin associations
- ID (generated)
- AlgorithmID (Foreign Key in Algorithm Table)
- Aggressiveness (Score of 0-1)
- Value (Total Value in $)

## tradingPoolCoinData
#### Keeps Track of Coin and USD amounts associated with each pool
- ID (generated)
- TradingPoolID (Foreign Key in TradingPools Table)
- CoinID (string)
- CoinAmount (Number of coins held in that pool)

## tradingPoolUserData
#### Stores User Investment Data
- ID (generated)
- UserID (Foreign Key in Users Table)
- TradingPoolID (Foreign Key in TradingPools Table)
- Amount (Percentage of pool owned)

## trades
#### Stores information about caluculated and executed trades
- ID (generated)
- TradingPoolID (Foreign Key in TradingPools Table)
- CoinFrom (string)
- CoinTo (string)
- Amt (In $)
- ExchangeID (string)
- Completed (bit is 1 if completed)
