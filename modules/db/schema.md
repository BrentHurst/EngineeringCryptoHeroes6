# Database Layout

## coins
#### An identifier table for coins that are tradable
- coinID (generated)
- name

## exchanges
#### An identifier table for exchanges that are tradable
- exchangeID (generated)
- Exchange Name

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
- CoinID (Foreign Key in Coin table)
- ExchangeID (Foreign Key in Exchange table)
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
- CoinID (Foreign Key in Coin table)
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
- CoinFrom (Foreign Key in Coin Table)
- CoinTo (Foreign Key in Coin Table)
- Amt (In $)
- ExchangeID (Foreign Key in Exchange Table)
- Completed (bit is 1 if completed)
