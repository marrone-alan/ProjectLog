# A log consult to show info about articles, authors and requests.

from flask import Flask, request, redirect, url_for

from newsdb import getTitles, getAuthors, getPercentage

app = Flask(__name__)

# HTML template for the log results
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Log Project</title>
  </head>
  <body>
    <table>
      <thead>
        <th colspan="2">
          Three most popular articles of all time
        </th>
      </thead>
      <tbody>
{0}
      </tbody>
    </table>
    <table>
      <thead>
        <th colspan="2">
    Authors of the most popular articles of all time
        </th>
      </thead>
      <tbody>
{1}
      </tbody>
    </table>
    <p><em>Days where more than 1% of requests resulted in errors<em></p>
{2}
  </body>

</html>
'''

# td fot the authors and titles
TD = '''\
    <tr><td>{0}</td><td>{1} Views</td></tr>
'''

# p for the errors
P = '''
    <p>%s - %s</p>
'''


@app.route('/', methods=['GET'])
def main():
    '''Main page.'''
    table1 = "".join(TD.format(views, title) for views, title in getTitles())
    table2 = "".join(TD.format(views, name) for views, name in getAuthors())
    percentage = "".join(P % (error, day) for error, day in getPercentage())
    html = HTML_WRAP.format(table1, table2, percentage)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
