# %%
import asyncio
import sys
import os

sys.path.append("./src")
from tradingapi.alpaca.alpaca_api import AlpacaApi

print(os.getcwd())

# %%

async def main() -> None:

    api_settings = {
            "APCA_API_KEY_ID": "PK8HDG7R05LLSH8YM25W",
            "APCA_API_SECRET_KEY": "tthYbkvPYymnDuQJDYsdmfZ7v9lFmec2KRal0tYF",
            "APCA_API_BASE_URL": "https://paper-api.alpaca.markets",
            "APCA_RETRY_MAX": "3"
    }

    api = AlpacaApi(api_settings)

    # Create an order to test on 
    #take_profit = {
    #"limit_price": "3000.00"
    #}
    #stop_loss = {"stop_price": "297.95", "limit_price": "290.95"}
    #test_order = await api.api.submit_order("TSLA", 10, side="buy", type="market", time_in_force="day", take_profit=take_profit, order_class="bracket", stop_loss=stop_loss)

    # [TODO]list_orders
    # List all orders
    orders = await api.list_orders()
    print(orders)
    #[x.__dict__ for x in orders]

    # [TODO]get_order
    # Add a order id or submit 
    #order = await api.get_order(test_order)
    #order.__dict__ 



    # [TODO]cancel_order
    # [TODO]cancel_all_orders
    # [TODO]list_positions
    # [TODO]get_position
    # [TODO]close_position
    # [TODO] close_all_positions

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
