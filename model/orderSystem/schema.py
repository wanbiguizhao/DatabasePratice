class Dish:
    id:int 
    uuid:str
    caixi:["鲁菜"] # https://www.chushixiu.cn/21175.html
    price:float 
    inventory_amount:int # 设置锁的情况。
    comment:str 
    tags: str 




class OrderItem:
    createdate:datetime
    id:int
    uuid:str
    dish_obj:Dish
    status:["已做","没做","作废"]
    amount:int
    price:float


class Order:
    """订单"""
    createdata:date 
    start_time:datetime
    end_time:datetime
    id:int
    uuid: str  
    table_id: int  
    #order_item_list:List[OrderItem]
    final_price:float 
    origin_price:float
    status:["点菜","上菜","结账","离开"]



class DiningTable:
    """
    餐桌。
    """
    id:int 
    status:["free","useing"]
### 可以把这些订单，这个是OOD设计，并不是真正的变成数据库的累。
### 想好一些redis缓存的情况，锁相关的情况。 快速生成500w的订单，进行数据分析。
### 


