from flask import Flask, request, jsonify, make_response
from persistence import Persistence
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def get_category(category):
    if (category == "localnews"):
        return "'ሀገር አቀፍ ዜና'"
    elif (category == "sport"):
        return "'ስፖርት'"
    elif (category == "poletics"):
        return "'ፖለቲካ'"
    elif (category == "entertiement"):
        return "'መዝናኛ'"
    elif (category == "5"):
        return "'ዓለም አቀፍ ዜና'"
    elif (category == "business"):
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