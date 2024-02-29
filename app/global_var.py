global obj
obj = {
    'cookie': '',
    'bvid': '',
    'cid': '',
    'page': '',
    'pagelist': '',
    'sub_list': '',
    'sub': '',
    'text': '',
}
    
def set_obj(item: str, new):
    global obj
    obj[item] = new

def get_obj(item:str):
    return obj[item]