# Database Layout

## Coin
#### An identifier table for coins that are tradable
- ID (generated)
- Coin Name

## Exchange
#### An identifier table for exchanges that are tradable
- ID (generated)
- Exchange Name

## CryptoData
#### Stores Current Market State
- ID (generated)
- CoinID (Foreign Key in Coin table)
- ExchangeID (Foreign Key in Exchange table)
- Value (in $/coin)
- Timestamp

## TradingPools
#### Keeps track of trading pools values and coin associations
- ID (generated)
- AlgorithmID (Foreign Key in Algorithm Table)
- Aggressiveness (Score of 0-1)
- Value (Total Value in $)

## TradingPoolCoinData
#### Keeps Track of Coin and USD amounts associated with each pool
- ID (generated)
- TradingPoolID (Foreign Key in TradingPools Table)
- CoinID (Foreign Key in Coin table)
- CoinAmount (Number of coins held in that pool)

## TradingPoolUserData
#### Stores User Investment Data
- ID (generated)
- UserID (Foreign Key in Users Table)
- TradingPoolID (Foreign Key in TradingPools Table)
- Amount (Percentage of pool owned)

## UserInfo
#### Store information about end users
- ID (generated)
- email (string)
- Name (string)
- ...

## Trades
#### Stores information about caluculated and executed trades
- ID (generated)
- TradingPoolID (Foreign Key in TradingPools Table)
- CoinFrom (Foreign Key in Coin Table)
- CoinTo (Foreign Key in Coin Table)
- Amt (In $)
- ExchangeID (Foreign Key in Exchange Table)
- Completed (bit is 1 if completed)
