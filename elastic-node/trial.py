from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch('crest-cache-01.cs.fiu.edu',port=81)


@app.route('/')
def home():
    return render_template('search.html')


@app.route('/search/results', methods=['GET', 'POST'])
def search_request():
    search_term = request.form["input"]
    res = es.search(
        index="proceedings",
        size=20,
        body={ 
            "query": 
            { "match" : 
            {"abstract":search_term}
            }
            })
    return render_template('results.html', res=res)

if __name__ == '__main__':
    app.secret_key='mysecret'
    app.run(host='0.0.0.0', port=9874)
