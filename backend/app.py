from flask import Flask, request, jsonify, make_response
from persistence import Persistence
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def get_category(num):
    if (num == "1"):
        return "'ሀገር አቀፍ ዜና'"
    elif (num == "2"):
        return "'ስፖርት'"
    elif (num == "3"):
        return "'ፖለቲካ'"
    elif (num == "4"):
        return "'መዝናኛ'"
    elif (num == "5"):
        return "'ዓለም አቀፍ ዜና'"
    elif (num == "6"):
        return "'ቢዝነስ'"

@app.route('/news/<category>', methods =['GET'])
def getNews(category):
    persist = Persistence()
    category = get_category(category)
    news = persist.select_data(category)
    output = {
        'uuid': news[0],
        'headline': news[1]
    }
    return jsonify({'news': output})

if __name__ == "__main__":
	app.run(debug = True)