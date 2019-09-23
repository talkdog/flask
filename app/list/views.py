from . import list
@list.route("/list",methods=['POST','GET'])
def test():
    return "我是測試的"