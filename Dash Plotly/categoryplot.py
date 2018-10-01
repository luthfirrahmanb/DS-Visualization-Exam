import plotly.graph_objs as go
from data import dfTitanic

listGoFunc = {
    'bar': go.Bar,
    'violin': go.Violin,
    'box': go.Box
}

def getPlot(jenis, xCategory):
    return [
        listGoFunc[jenis](
            x=dfTitanic[xCategory],
            y=dfTitanic['fare'],
            # text=dfTitanic['day'],
            opacity=0.7,
            name='Fare',
            marker=dict(color='blue'),
            legendgroup = 'fare'
        ),
        listGoFunc[jenis](
            x=dfTitanic[xCategory],
            y=dfTitanic['age'],
            # text=dfTitanic['day'],
            opacity=0.7,
            name='Age',
            marker=dict(color='orange'),
            legendgroup = 'age'
        )
    ]