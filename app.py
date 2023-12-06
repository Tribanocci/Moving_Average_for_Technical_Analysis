from flask import Flask, render_template, request
import plotly.express as px
from MApolicy import *



app = Flask(__name__)
path_fig_input='static/plot_input.html'
path_fig_result='static/plot_results.html'
path_fig_data='static/plot_data.html'
stock_data_path = "static/stock_csv/"


def plot_csv(filename):
    res=csv_to_df(stock_data_path+filename, 1)
    fig=px.line(res, x='Date', y='Close')
    fig.write_html(path_fig_data)
    return filename


def algorithm(path_fig_input, path_fig_result):
    res1,res2=MA_policy(1000,0.6,10,1,365,8)
    
    fig1 = px.line(res1, color="Mean Average(MA)", 
                   title="Actual and prediction closing values of the stock")
    fig2 = px.line(res2, color="Mean Average(MA)", 
                   title="Result - Policy Outcome (Capital in currency)")
    fig1.update_layout(yaxis_title="Capital (in currency)", overwrite=True)
    fig1.update_layout(yaxis_title="Closing value", overwrite=True)
    fig1.write_html(path_fig_result)
    fig2.write_html(path_fig_input)


@app.route('/')
def index():
    fig_data=plot_csv("GE.csv")
    # Render the HTML template with the image
    return render_template('index.html', path_fig_input=path_fig_input, path_fig_result=path_fig_result, fig_data=fig_data, parameters=0, result=0)



@app.route('/', methods=['POST'])
def update():
    form_id  = request.form.get('form_selected')
    print(form_id)
    if form_id == 'update_data':
        print('hey')
        return update_data(request.form)
    elif form_id =='update_results':
        return update_results(request.form)
    else:
        return render_template('index.html', path_fig_input=path_fig_input, path_fig_result=path_fig_result, parameters=0, result=0)



def update_data(form_data):
    print('hey')
    data_filename = form_data.get('selected_value')
    print(data_filename)
    fig_data=plot_csv(data_filename)
    return render_template('index.html', path_fig_input=path_fig_input, path_fig_result=path_fig_result, fig_data=fig_data, parameters=0, result=0)


def update_results(form_data):
    print('einai kai edo')
    k = int(form_data.get('cell_k'))
    kefalaio = float(form_data.get('cell_kefalaio'))
    B = float(form_data.get('cell_B'))
    wait = int(form_data.get('cell_wait'))
    N = form_data.get('cell_N')
    if N == '':
        N=0
    else:
        N=int(N)
    data=form_data.get('data_selected')
    parameters = [ kefalaio, B, wait, k, N]
    #res1,res2=MA_policy(1000,0.6,8,1,365,10)
    file_path=stock_data_path+data
    print("my data", data)
    res1,res2=MA_policy(kefalaio,B,wait,1,365,k,file_path)
    fig1 = px.line(res1)
    fig2 = px.line(res2)
    #,'y':1.5,'x':0.5,'xanchor': 'center','yanchor': 'top'
    fig1.update_layout( title={'text': "Result - Policy outcome (Capital in currency)"}, 
                       yaxis_title="Capital (in currency)", 
                       legend_title="Moving Average (MA)", overwrite=True)
    fig2.update_layout(title="Actual and prediction closing values of the stock", 
                       yaxis_title="Closing value", 
                       legend_title="Moving Average (MA)", overwrite=True)

    fig1.write_html(path_fig_result)
    fig2.write_html(path_fig_input)
    table_results = [res1.iloc[len(res1)-1,0], res1.iloc[len(res1)-1,1], res1.iloc[len(res1)-1,2]]
    print(table_results)
    return render_template('index.html', path_fig_input=path_fig_input, path_fig_result=path_fig_result, parameters=parameters, result=1, fig_data=data, table_results=table_results)



if __name__ == '__main__':
    app.run(debug=True)