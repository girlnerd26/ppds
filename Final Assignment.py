{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p style=\"text-align:center\">\n",
    "    <a href=\"https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork900-2022-01-01\" target=\"_blank\">\n",
    "    <img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png\" width=\"200\" alt=\"Skills Network Logo\">\n",
    "    </a>\n",
    "</p>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>Extracting and Visualizing Stock Data</h1>\n",
    "<h2>Description</h2>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Extracting essential data from a dataset and displaying it is a necessary part of data science; therefore individuals can make correct decisions based on the data. In this assignment, you will extract some stock data, you will then display this data in a graph.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2>Table of Contents</h2>\n",
    "<div class=\"alert alert-block alert-info\" style=\"margin-top: 20px\">\n",
    "    <ul>\n",
    "        <li>Define a Function that Makes a Graph</li>\n",
    "        <li>Question 1: Use yfinance to Extract Stock Data</li>\n",
    "        <li>Question 2: Use Webscraping to Extract Tesla Revenue Data</li>\n",
    "        <li>Question 3: Use yfinance to Extract Stock Data</li>\n",
    "        <li>Question 4: Use Webscraping to Extract GME Revenue Data</li>\n",
    "        <li>Question 5: Plot Tesla Stock Graph</li>\n",
    "        <li>Question 6: Plot GameStop Stock Graph</li>\n",
    "    </ul>\n",
    "<p>\n",
    "    Estimated Time Needed: <strong>30 min</strong></p>\n",
    "</div>\n",
    "\n",
    "<hr>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "***Note***:- If you are working Locally using anaconda, please uncomment the following code and execute it.\n",
    "Use the version as per your python version.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: yfinance in /opt/conda/lib/python3.11/site-packages (0.2.49)\n",
      "Requirement already satisfied: pandas>=1.3.0 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2.2.3)\n",
      "Requirement already satisfied: numpy>=1.16.5 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2.1.3)\n",
      "Requirement already satisfied: requests>=2.31 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2.31.0)\n",
      "Requirement already satisfied: multitasking>=0.0.7 in /opt/conda/lib/python3.11/site-packages (from yfinance) (0.0.11)\n",
      "Requirement already satisfied: lxml>=4.9.1 in /opt/conda/lib/python3.11/site-packages (from yfinance) (5.3.0)\n",
      "Requirement already satisfied: platformdirs>=2.0.0 in /opt/conda/lib/python3.11/site-packages (from yfinance) (4.2.1)\n",
      "Requirement already satisfied: pytz>=2022.5 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2024.1)\n",
      "Requirement already satisfied: frozendict>=2.3.4 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2.4.6)\n",
      "Requirement already satisfied: peewee>=3.16.2 in /opt/conda/lib/python3.11/site-packages (from yfinance) (3.17.7)\n",
      "Requirement already satisfied: beautifulsoup4>=4.11.1 in /opt/conda/lib/python3.11/site-packages (from yfinance) (4.12.3)\n",
      "Requirement already satisfied: html5lib>=1.1 in /opt/conda/lib/python3.11/site-packages (from yfinance) (1.1)\n",
      "Requirement already satisfied: soupsieve>1.2 in /opt/conda/lib/python3.11/site-packages (from beautifulsoup4>=4.11.1->yfinance) (2.5)\n",
      "Requirement already satisfied: six>=1.9 in /opt/conda/lib/python3.11/site-packages (from html5lib>=1.1->yfinance) (1.16.0)\n",
      "Requirement already satisfied: webencodings in /opt/conda/lib/python3.11/site-packages (from html5lib>=1.1->yfinance) (0.5.1)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /opt/conda/lib/python3.11/site-packages (from pandas>=1.3.0->yfinance) (2.9.0)\n",
      "Requirement already satisfied: tzdata>=2022.7 in /opt/conda/lib/python3.11/site-packages (from pandas>=1.3.0->yfinance) (2024.2)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (2.2.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (2024.6.2)\n",
      "Requirement already satisfied: bs4 in /opt/conda/lib/python3.11/site-packages (0.0.2)\n",
      "Requirement already satisfied: beautifulsoup4 in /opt/conda/lib/python3.11/site-packages (from bs4) (4.12.3)\n",
      "Requirement already satisfied: soupsieve>1.2 in /opt/conda/lib/python3.11/site-packages (from beautifulsoup4->bs4) (2.5)\n",
      "Requirement already satisfied: nbformat in /opt/conda/lib/python3.11/site-packages (5.10.4)\n",
      "Requirement already satisfied: fastjsonschema>=2.15 in /opt/conda/lib/python3.11/site-packages (from nbformat) (2.19.1)\n",
      "Requirement already satisfied: jsonschema>=2.6 in /opt/conda/lib/python3.11/site-packages (from nbformat) (4.22.0)\n",
      "Requirement already satisfied: jupyter-core!=5.0.*,>=4.12 in /opt/conda/lib/python3.11/site-packages (from nbformat) (5.7.2)\n",
      "Requirement already satisfied: traitlets>=5.1 in /opt/conda/lib/python3.11/site-packages (from nbformat) (5.14.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (23.2.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (2023.12.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (0.35.1)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (0.18.0)\n",
      "Requirement already satisfied: platformdirs>=2.5 in /opt/conda/lib/python3.11/site-packages (from jupyter-core!=5.0.*,>=4.12->nbformat) (4.2.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install yfinance\n",
    "!pip install bs4\n",
    "!pip install nbformat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import yfinance as yf\n",
    "import pandas as pd\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import plotly.graph_objects as go\n",
    "from plotly.subplots import make_subplots"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In Python, you can ignore warnings using the warnings module. You can use the filterwarnings function to filter or ignore specific warning messages or categories.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "# Ignore all warnings\n",
    "warnings.filterwarnings(\"ignore\", category=FutureWarning)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Define Graphing Function\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this section, we define the function `make_graph`. **You don't have to know how the function works, you should only care about the inputs. It takes a dataframe with stock data (dataframe must contain Date and Close columns), a dataframe with revenue data (dataframe must contain Date and Revenue columns), and the name of the stock.**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def make_graph(stock_data, revenue_data, stock):\n",
    "    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=(\"Historical Share Price\", \"Historical Revenue\"), vertical_spacing = .3)\n",
    "    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']\n",
    "    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']\n",
    "    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype(\"float\"), name=\"Share Price\"), row=1, col=1)\n",
    "    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype(\"float\"), name=\"Revenue\"), row=2, col=1)\n",
    "    fig.update_xaxes(title_text=\"Date\", row=1, col=1)\n",
    "    fig.update_xaxes(title_text=\"Date\", row=2, col=1)\n",
    "    fig.update_yaxes(title_text=\"Price ($US)\", row=1, col=1)\n",
    "    fig.update_yaxes(title_text=\"Revenue ($US Millions)\", row=2, col=1)\n",
    "    fig.update_layout(showlegend=False,\n",
    "    height=900,\n",
    "    title=stock,\n",
    "    xaxis_rangeslider_visible=True)\n",
    "    fig.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the make_graph function that we’ve already defined. You’ll need to invoke it in questions 5 and 6 to display the graphs and create the dashboard. \n",
    "> **Note: You don’t need to redefine the function for plotting graphs anywhere else in this notebook; just use the existing function.**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 1: Use yfinance to Extract Stock Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the `Ticker` function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is Tesla and its ticker symbol is `TSLA`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "import yfinance as yf\n",
    "\n",
    "# Create a ticker object for Tesla (TSLA)\n",
    "tesla = yf.Ticker(\"TSLA\")\n",
    "\n",
    "# Now you can extract various data points about Tesla, for example:\n",
    "tesla_info = tesla.info  # General information about Tesla\n",
    "tesla_history = tesla.history(period=\"1d\")  # Tesla stock history for the last day"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the ticker object and the function `history` extract stock information and save it in a dataframe named `tesla_data`. Set the `period` parameter to ` \"max\" ` so we get information for the maximum amount of time.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                               Open      High       Low     Close     Volume  \\\n",
      "Date                                                                           \n",
      "2010-06-29 00:00:00-04:00  1.266667  1.666667  1.169333  1.592667  281494500   \n",
      "2010-06-30 00:00:00-04:00  1.719333  2.028000  1.553333  1.588667  257806500   \n",
      "2010-07-01 00:00:00-04:00  1.666667  1.728000  1.351333  1.464000  123282000   \n",
      "2010-07-02 00:00:00-04:00  1.533333  1.540000  1.247333  1.280000   77097000   \n",
      "2010-07-06 00:00:00-04:00  1.333333  1.333333  1.055333  1.074000  103003500   \n",
      "\n",
      "                           Dividends  Stock Splits  \n",
      "Date                                                \n",
      "2010-06-29 00:00:00-04:00        0.0           0.0  \n",
      "2010-06-30 00:00:00-04:00        0.0           0.0  \n",
      "2010-07-01 00:00:00-04:00        0.0           0.0  \n",
      "2010-07-02 00:00:00-04:00        0.0           0.0  \n",
      "2010-07-06 00:00:00-04:00        0.0           0.0  \n"
     ]
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "\n",
    "# Create a ticker object for Tesla (TSLA)\n",
    "tesla = yf.Ticker(\"TSLA\")\n",
    "\n",
    "# Extract the stock data for the maximum period and save it in a DataFrame\n",
    "tesla_data = tesla.history(period=\"max\")\n",
    "\n",
    "# Display the first few rows of the DataFrame\n",
    "print(tesla_data.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Reset the index** using the `reset_index(inplace=True)` function on the tesla_data DataFrame and display the first five rows of the `tesla_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 1 to the results below.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                       Date      Open      High       Low     Close  \\\n",
      "0 2010-06-29 00:00:00-04:00  1.266667  1.666667  1.169333  1.592667   \n",
      "1 2010-06-30 00:00:00-04:00  1.719333  2.028000  1.553333  1.588667   \n",
      "2 2010-07-01 00:00:00-04:00  1.666667  1.728000  1.351333  1.464000   \n",
      "3 2010-07-02 00:00:00-04:00  1.533333  1.540000  1.247333  1.280000   \n",
      "4 2010-07-06 00:00:00-04:00  1.333333  1.333333  1.055333  1.074000   \n",
      "\n",
      "      Volume  Dividends  Stock Splits  \n",
      "0  281494500        0.0           0.0  \n",
      "1  257806500        0.0           0.0  \n",
      "2  123282000        0.0           0.0  \n",
      "3   77097000        0.0           0.0  \n",
      "4  103003500        0.0           0.0  \n"
     ]
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "\n",
    "# Create a ticker object for Tesla (TSLA)\n",
    "tesla = yf.Ticker(\"TSLA\")\n",
    "\n",
    "# Extract the stock data for the maximum period and save it in a DataFrame\n",
    "tesla_data = tesla.history(period=\"max\")\n",
    "\n",
    "# Reset the index\n",
    "tesla_data.reset_index(inplace=True)\n",
    "\n",
    "# Display the first five rows of the DataFrame\n",
    "print(tesla_data.head())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 2: Use Webscraping to Extract Tesla Revenue Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `requests` library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm Save the text of the response as a variable named `html_data`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "<!DOCTYPE html>\n",
      "<!--[if lt IE 7]>      <html class=\"no-js lt-ie9 lt-ie8 lt-ie7\"> <![endif]-->\n",
      "<!--[if IE 7]>         <html class=\"no-js lt-ie9 lt-ie8\"> <![endif]-->\n",
      "<!--[if IE 8]>         <html class=\"no-js lt-ie9\"> <![endif]-->\n",
      "<!--[if gt IE 8]><!--> <html class=\"no-js\"> <!--<![endif]-->\n",
      "    <head>\n",
      "        <meta charset=\"utf-8\">\n",
      "        <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">\n",
      "\t\t<link rel=\"canonical\" href=\"https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue\" />\n",
      "\t\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "# URL of the webpage to download\n",
    "url = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm\"\n",
    "\n",
    "# Send a GET request to the URL\n",
    "response = requests.get(url)\n",
    "\n",
    "# Save the text of the response to the variable 'html_data'\n",
    "html_data = response.text\n",
    "\n",
    "# Optionally, print the first 500 characters of the HTML data to verify\n",
    "print(html_data[:500])  # Print the first 500 characters of the HTML\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Parse the html data using `beautiful_soup` using parser i.e `html5lib` or `html.parser`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<!DOCTYPE html>\n",
      "<!--[if lt IE 7]>      <html class=\"no-js lt-ie9 lt-ie8 lt-ie7\"> <![endif]-->\n",
      "<!--[if IE 7]>         <html class=\"no-js lt-ie9 lt-ie8\"> <![endif]-->\n",
      "<!--[if IE 8]>         <html class=\"no-js lt-ie9\"> <![endif]-->\n",
      "<!--[if gt IE 8]><!-->\n",
      "<html class=\"no-js\">\n",
      " <!--<![endif]-->\n",
      " <head>\n",
      "  <meta charset=\"utf-8\"/>\n",
      "  <meta content=\"IE=edge,chrome=1\" http-equiv=\"X-UA-Compatible\"/>\n",
      "  <link href=\"https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue\" rel=\"canonical\"/>\n",
      "  <title>\n",
      "   Te\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "# URL of the webpage to download\n",
    "url = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm\"\n",
    "\n",
    "# Send a GET request to the URL\n",
    "response = requests.get(url)\n",
    "\n",
    "# Save the text of the response to the variable 'html_data'\n",
    "html_data = response.text\n",
    "\n",
    "# Parse the HTML data using BeautifulSoup with the 'html.parser' parser\n",
    "soup = BeautifulSoup(html_data, 'html.parser')  # Alternatively, use 'html5lib' as the parser\n",
    "\n",
    "# To verify, let's print out the parsed HTML (first 500 characters)\n",
    "print(soup.prettify()[:500])  # prettify makes the HTML output more readable"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using `BeautifulSoup` or the `read_html` function extract the table with `Tesla Revenue` and store it into a dataframe named `tesla_revenue`. The dataframe should have columns `Date` and `Revenue`.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Step-by-step instructions</summary>\n",
    "\n",
    "```\n",
    "\n",
    "Here are the step-by-step instructions:\n",
    "\n",
    "1. Create an Empty DataFrame\n",
    "2. Find the Relevant Table\n",
    "3. Check for the Tesla Quarterly Revenue Table\n",
    "4. Iterate Through Rows in the Table Body\n",
    "5. Extract Data from Columns\n",
    "6. Append Data to the DataFrame\n",
    "\n",
    "```\n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Click here if you need help locating the table</summary>\n",
    "\n",
    "```\n",
    "    \n",
    "Below is the code to isolate the table, you will now need to loop through the rows and columns like in the previous lab\n",
    "    \n",
    "soup.find_all(\"tbody\")[1]\n",
    "    \n",
    "If you want to use the read_html function the table is located at index 1\n",
    "\n",
    "We are focusing on quarterly revenue in the lab.\n",
    "```\n",
    "\n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Tesla Annual Revenue (Millions of US $)  \\\n",
      "0                                     2021   \n",
      "1                                     2020   \n",
      "2                                     2019   \n",
      "3                                     2018   \n",
      "4                                     2017   \n",
      "\n",
      "  Tesla Annual Revenue (Millions of US $).1  \n",
      "0                                   $53,823  \n",
      "1                                   $31,536  \n",
      "2                                   $24,578  \n",
      "3                                   $21,461  \n",
      "4                                   $11,759  \n",
      "   Date  Revenue\n",
      "0  2021  $53,823\n",
      "1  2020  $31,536\n",
      "2  2019  $24,578\n",
      "3  2018  $21,461\n",
      "4  2017  $11,759\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "# URL of the webpage to download\n",
    "url = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm\"\n",
    "\n",
    "# Send a GET request to the URL\n",
    "response = requests.get(url)\n",
    "\n",
    "# Parse the HTML data using BeautifulSoup\n",
    "soup = BeautifulSoup(response.text, 'html.parser')\n",
    "\n",
    "# Find all the tables in the HTML\n",
    "tables = pd.read_html(str(soup))  # This reads all tables from the HTML as a list of DataFrames\n",
    "\n",
    "# Since there may be multiple tables, let's check which one contains Tesla Revenue.\n",
    "# The table we want might be the first one or another one. You can inspect the tables if needed.\n",
    "\n",
    "# Assuming the first table is the one with the relevant data\n",
    "tesla_revenue = tables[0]  # Adjust the index if the target table is not the first one\n",
    "\n",
    "# Display the first few rows of the DataFrame to inspect\n",
    "print(tesla_revenue.head())\n",
    "\n",
    "# Rename columns to match the desired format: Date and Revenue\n",
    "tesla_revenue.columns = ['Date', 'Revenue']\n",
    "\n",
    "# Display the DataFrame\n",
    "print(tesla_revenue.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Execute the following line to remove the comma and dollar sign from the `Revenue` column. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Date  Revenue\n",
      "0  2021    53823\n",
      "1  2020    31536\n",
      "2  2019    24578\n",
      "3  2018    21461\n",
      "4  2017    11759\n"
     ]
    }
   ],
   "source": [
    "# Remove commas and dollar signs from the 'Revenue' column\n",
    "tesla_revenue['Revenue'] = tesla_revenue['Revenue'].replace({'\\$': '', ',': ''}, regex=True)\n",
    "\n",
    "# Convert the 'Revenue' column to numeric (float type)\n",
    "tesla_revenue['Revenue'] = pd.to_numeric(tesla_revenue['Revenue'])\n",
    "\n",
    "# Display the DataFrame to confirm the changes\n",
    "print(tesla_revenue.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Execute the following lines to remove an null or empty strings in the Revenue column.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Date  Revenue\n",
      "0  2021    53823\n",
      "1  2020    31536\n",
      "2  2019    24578\n",
      "3  2018    21461\n",
      "4  2017    11759\n"
     ]
    }
   ],
   "source": [
    "# Remove rows where 'Revenue' is NaN or an empty string\n",
    "tesla_revenue = tesla_revenue[tesla_revenue['Revenue'].notna()]  # Remove NaN values\n",
    "tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != '']  # Remove empty strings\n",
    "\n",
    "# Display the DataFrame to confirm the changes\n",
    "print(tesla_revenue.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Display the last 5 row of the `tesla_revenue` dataframe using the `tail` function. Take a screenshot of the results.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Date  Revenue\n",
      "8   2013     2013\n",
      "9   2012      413\n",
      "10  2011      204\n",
      "11  2010      117\n",
      "12  2009      112\n"
     ]
    }
   ],
   "source": [
    "# Display the last 5 rows of the DataFrame using the tail() function\n",
    "print(tesla_revenue.tail())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 3: Use yfinance to Extract Stock Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the `Ticker` function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is GameStop and its ticker symbol is `GME`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'address1': '625 Westport Parkway', 'city': 'Grapevine', 'state': 'TX', 'zip': '76051', 'country': 'United States', 'phone': '817 424 2000', 'website': 'https://www.gamestop.com', 'industry': 'Specialty Retail', 'industryKey': 'specialty-retail', 'industryDisp': 'Specialty Retail', 'sector': 'Consumer Cyclical', 'sectorKey': 'consumer-cyclical', 'sectorDisp': 'Consumer Cyclical', 'longBusinessSummary': 'GameStop Corp., a specialty retailer, provides games and entertainment products through its stores and ecommerce platforms in the United States, Canada, Australia, and Europe. The company sells new and pre-owned gaming platforms; accessories, such as controllers, gaming headsets, and virtual reality products; new and pre-owned gaming software; and in-game digital currency, digital downloadable content, and full-game downloads. It sells collectibles comprising apparel, toys, trading cards, gadgets, and other retail products for pop culture and technology enthusiasts, as well as engages in the digital asset wallet and NFT marketplace activities. The company operates stores and ecommerce sites under the GameStop, EB Games, and Micromania brands; and pop culture themed stores that sell collectibles, apparel, gadgets, electronics, toys, and other retail products under the Zing Pop Culture brand, as well as offers Game Informer magazine, a print and digital gaming publication. The company was formerly known as GSC Holdings Corp. GameStop Corp. was founded in 1996 and is headquartered in Grapevine, Texas.', 'fullTimeEmployees': 8000, 'companyOfficers': [{'maxAge': 1, 'name': 'Mr. Ryan  Cohen', 'age': 37, 'title': 'President, CEO & Executive Chairman', 'yearBorn': 1986, 'fiscalYear': 2023, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Daniel William Moore', 'age': 40, 'title': 'Principal Accounting Officer & Principal Financial Officer', 'yearBorn': 1983, 'fiscalYear': 2023, 'totalPay': 277711, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Mark Haymond Robinson', 'age': 45, 'title': 'General Counsel & Secretary', 'yearBorn': 1978, 'fiscalYear': 2023, 'totalPay': 337657, 'exercisedValue': 0, 'unexercisedValue': 0}], 'auditRisk': 8, 'boardRisk': 6, 'compensationRisk': 7, 'shareHolderRightsRisk': 3, 'overallRisk': 5, 'governanceEpochDate': 1730419200, 'compensationAsOfEpochDate': 1703980800, 'irWebsite': 'http://phx.corporate-ir.net/phoenix.zhtml?c=130125&p=irol-irhome', 'maxAge': 86400, 'priceHint': 2, 'previousClose': 24.88, 'open': 25.26, 'dayLow': 24.6271, 'dayHigh': 28.04, 'regularMarketPreviousClose': 24.88, 'regularMarketOpen': 25.26, 'regularMarketDayLow': 24.6271, 'regularMarketDayHigh': 28.04, 'exDividendDate': 1552521600, 'fiveYearAvgDividendYield': 9.52, 'beta': -0.098, 'trailingPE': 194.71428, 'forwardPE': -2726.0, 'volume': 25559563, 'regularMarketVolume': 25559563, 'averageVolume': 8329922, 'averageVolume10days': 8464520, 'averageDailyVolume10Day': 8464520, 'bidSize': 800, 'askSize': 1100, 'marketCap': 12171863040, 'fiftyTwoWeekLow': 9.95, 'fiftyTwoWeekHigh': 64.83, 'priceToSalesTrailing12Months': 2.6739593, 'fiftyDayAverage': 21.8132, 'twoHundredDayAverage': 19.848, 'currency': 'USD', 'enterpriseValue': 7955951616, 'profitMargins': 0.00934, 'floatShares': 390217891, 'sharesOutstanding': 446510016, 'sharesShort': 35962132, 'sharesShortPriorMonth': 36551732, 'sharesShortPreviousMonthDate': 1726185600, 'dateShortInterest': 1728950400, 'sharesPercentSharesOut': 0.0805, 'heldPercentInsiders': 0.08495, 'heldPercentInstitutions': 0.22622, 'shortRatio': 3.83, 'shortPercentOfFloat': 0.096599996, 'impliedSharesOutstanding': 446510016, 'bookValue': 10.278, 'priceToBook': 2.652267, 'lastFiscalYearEnd': 1706918400, 'nextFiscalYearEnd': 1738540800, 'mostRecentQuarter': 1722643200, 'netIncomeToCommon': 42500000, 'trailingEps': 0.14, 'forwardEps': -0.01, 'pegRatio': 16.23, 'lastSplitFactor': '4:1', 'lastSplitDate': 1658448000, 'enterpriseToRevenue': 1.748, 'enterpriseToEbitda': 168.558, '52WeekChange': 0.9286822, 'SandP52WeekChange': 0.3336166, 'lastDividendValue': 0.095, 'lastDividendDate': 1552521600, 'exchange': 'NYQ', 'quoteType': 'EQUITY', 'symbol': 'GME', 'underlyingSymbol': 'GME', 'shortName': 'GameStop Corporation', 'longName': 'GameStop Corp.', 'firstTradeDateEpochUtc': 1013610600, 'timeZoneFullName': 'America/New_York', 'timeZoneShortName': 'EST', 'uuid': '8ded85bd-8171-3e2e-afa6-c81272285147', 'messageBoardId': 'finmb_1342560', 'gmtOffSetMilliseconds': -18000000, 'currentPrice': 27.26, 'targetHighPrice': 10.0, 'targetLowPrice': 5.75, 'targetMeanPrice': 7.88, 'targetMedianPrice': 7.88, 'recommendationMean': 4.5, 'recommendationKey': 'underperform', 'numberOfAnalystOpinions': 2, 'totalCash': 4204199936, 'totalCashPerShare': 9.857, 'ebitda': 47200000, 'totalDebt': 533500000, 'quickRatio': 5.442, 'currentRatio': 6.233, 'totalRevenue': 4552000000, 'debtToEquity': 12.171, 'revenuePerShare': 13.97, 'returnOnAssets': 0.00043000001, 'returnOnEquity': 0.015039999, 'freeCashflow': -93387504, 'operatingCashflow': -33100000, 'revenueGrowth': -0.314, 'grossMargins': 0.26237, 'ebitdaMargins': 0.010369999, 'operatingMargins': -0.03558, 'financialCurrency': 'USD', 'trailingPegRatio': None}\n"
     ]
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "\n",
    "# Create a ticker object for GameStop (GME)\n",
    "gamestop = yf.Ticker(\"GME\")\n",
    "\n",
    "# To verify, you can print some basic information about the stock\n",
    "print(gamestop.info)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the ticker object and the function `history` extract stock information and save it in a dataframe named `gme_data`. Set the `period` parameter to ` \"max\" ` so we get information for the maximum amount of time.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                               Open      High       Low     Close    Volume  \\\n",
      "Date                                                                          \n",
      "2002-02-13 00:00:00-05:00  1.620129  1.693350  1.603296  1.691667  76216000   \n",
      "2002-02-14 00:00:00-05:00  1.712707  1.716073  1.670626  1.683250  11021600   \n",
      "2002-02-15 00:00:00-05:00  1.683250  1.687458  1.658001  1.674834   8389600   \n",
      "2002-02-19 00:00:00-05:00  1.666418  1.666418  1.578047  1.607504   7410400   \n",
      "2002-02-20 00:00:00-05:00  1.615920  1.662210  1.603296  1.662210   6892800   \n",
      "\n",
      "                           Dividends  Stock Splits  \n",
      "Date                                                \n",
      "2002-02-13 00:00:00-05:00        0.0           0.0  \n",
      "2002-02-14 00:00:00-05:00        0.0           0.0  \n",
      "2002-02-15 00:00:00-05:00        0.0           0.0  \n",
      "2002-02-19 00:00:00-05:00        0.0           0.0  \n",
      "2002-02-20 00:00:00-05:00        0.0           0.0  \n"
     ]
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "\n",
    "# Create a ticker object for GameStop (GME)\n",
    "gamestop = yf.Ticker(\"GME\")\n",
    "\n",
    "# Extract the stock data for the maximum period and save it in a DataFrame\n",
    "gme_data = gamestop.history(period=\"max\")\n",
    "\n",
    "# Display the first few rows of the DataFrame\n",
    "print(gme_data.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Reset the index** using the `reset_index(inplace=True)` function on the gme_data DataFrame and display the first five rows of the `gme_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 3 to the results below.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                       Date      Open      High       Low     Close    Volume  \\\n",
      "0 2002-02-13 00:00:00-05:00  1.620128  1.693350  1.603296  1.691666  76216000   \n",
      "1 2002-02-14 00:00:00-05:00  1.712707  1.716074  1.670626  1.683250  11021600   \n",
      "2 2002-02-15 00:00:00-05:00  1.683251  1.687459  1.658002  1.674834   8389600   \n",
      "3 2002-02-19 00:00:00-05:00  1.666417  1.666417  1.578047  1.607504   7410400   \n",
      "4 2002-02-20 00:00:00-05:00  1.615921  1.662210  1.603296  1.662210   6892800   \n",
      "\n",
      "   Dividends  Stock Splits  \n",
      "0        0.0           0.0  \n",
      "1        0.0           0.0  \n",
      "2        0.0           0.0  \n",
      "3        0.0           0.0  \n",
      "4        0.0           0.0  \n"
     ]
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "\n",
    "# Create a ticker object for GameStop (GME)\n",
    "gamestop = yf.Ticker(\"GME\")\n",
    "\n",
    "# Extract the stock data for the maximum period and save it in a DataFrame\n",
    "gme_data = gamestop.history(period=\"max\")\n",
    "\n",
    "# Reset the index\n",
    "gme_data.reset_index(inplace=True)\n",
    "\n",
    "# Display the first five rows of the DataFrame\n",
    "print(gme_data.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 4: Use Webscraping to Extract GME Revenue Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `requests` library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html. Save the text of the response as a variable named `html_data_2`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<!DOCTYPE html>\n",
      "<!-- saved from url=(0105)https://web.archive.org/web/20200814131437/https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue -->\n",
      "<html class=\" js flexbox canvas canvastext webgl no-touch geolocation postmessage websqldatabase indexeddb hashchange history draganddrop websockets rgba hsla multiplebgs backgroundsize borderimage borderradius boxshadow textshadow opacity cssanimations csscolumns cssgradients cssreflections csstransforms csstransforms3d csstransitions fontface g\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "# URL of the webpage to download\n",
    "url = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html\"\n",
    "\n",
    "# Send a GET request to the URL\n",
    "response = requests.get(url)\n",
    "\n",
    "# Save the text of the response to the variable 'html_data_2'\n",
    "html_data_2 = response.text\n",
    "\n",
    "# Optionally, print the first 500 characters of the HTML data to verify\n",
    "print(html_data_2[:500])  # Print the first 500 characters of the HTML"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Parse the html data using `beautiful_soup` using parser i.e `html5lib` or `html.parser`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<!DOCTYPE html>\n",
      "<!-- saved from url=(0105)https://web.archive.org/web/20200814131437/https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue -->\n",
      "<html class=\"js flexbox canvas canvastext webgl no-touch geolocation postmessage websqldatabase indexeddb hashchange history draganddrop websockets rgba hsla multiplebgs backgroundsize borderimage borderradius boxshadow textshadow opacity cssanimations csscolumns cssgradients cssreflections csstransforms csstransforms3d csstransitions fontface ge\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "# URL of the webpage to download\n",
    "url = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html\"\n",
    "\n",
    "# Send a GET request to the URL\n",
    "response = requests.get(url)\n",
    "\n",
    "# Save the text of the response to the variable 'html_data_2'\n",
    "html_data_2 = response.text\n",
    "\n",
    "# Parse the HTML data using BeautifulSoup with the 'html.parser' parser\n",
    "soup = BeautifulSoup(html_data_2, 'html.parser')  # You can use 'html5lib' instead if you prefer\n",
    "\n",
    "# To verify, let's print out the parsed HTML (first 500 characters)\n",
    "print(soup.prettify()[:500])  # prettify makes the HTML output more readable"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using `BeautifulSoup` or the `read_html` function extract the table with `GameStop Revenue` and store it into a dataframe named `gme_revenue`. The dataframe should have columns `Date` and `Revenue`. Make sure the comma and dollar sign is removed from the `Revenue` column.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Note: Use the method similar to what you did in question 2.**  \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Click here if you need help locating the table</summary>\n",
    "\n",
    "```\n",
    "    \n",
    "Below is the code to isolate the table, you will now need to loop through the rows and columns like in the previous lab\n",
    "    \n",
    "soup.find_all(\"tbody\")[1]\n",
    "    \n",
    "If you want to use the read_html function the table is located at index 1\n",
    "\n",
    "\n",
    "```\n",
    "\n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date Revenue\n",
      "0  2020-04-30  $1,021\n",
      "1  2020-01-31  $2,194\n",
      "2  2019-10-31  $1,439\n",
      "3  2019-07-31  $1,286\n",
      "4  2019-04-30  $1,548\n",
      "         Date  Revenue\n",
      "0  2020-04-30     1021\n",
      "1  2020-01-31     2194\n",
      "2  2019-10-31     1439\n",
      "3  2019-07-31     1286\n",
      "4  2019-04-30     1548\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "\n",
    "# URL of the webpage\n",
    "url = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html\"\n",
    "\n",
    "# Send a GET request to the URL\n",
    "response = requests.get(url)\n",
    "\n",
    "# Parse the HTML data using BeautifulSoup\n",
    "soup = BeautifulSoup(response.text, 'html.parser')\n",
    "\n",
    "# Extract the second table body using the method provided\n",
    "table = soup.find_all(\"tbody\")[1]  # This is where the GameStop revenue table is located\n",
    "\n",
    "# Initialize lists to hold the data\n",
    "dates = []\n",
    "revenues = []\n",
    "\n",
    "# Loop through each row in the table\n",
    "for row in table.find_all('tr'):\n",
    "    # Extract the date and revenue from each row\n",
    "    cols = row.find_all('td')\n",
    "    if len(cols) == 2:  # Ensure the row has exactly two columns (Date, Revenue)\n",
    "        date = cols[0].text.strip()  # Get the Date\n",
    "        revenue = cols[1].text.strip()  # Get the Revenue\n",
    "\n",
    "        # Append the extracted data to the lists\n",
    "        dates.append(date)\n",
    "        revenues.append(revenue)\n",
    "\n",
    "# Create a DataFrame from the extracted data\n",
    "gme_revenue = pd.DataFrame({\n",
    "    'Date': dates,\n",
    "    'Revenue': revenues\n",
    "})\n",
    "\n",
    "# Display the first few rows of the DataFrame to inspect\n",
    "print(gme_revenue.head())\n",
    "\n",
    "# Clean the 'Revenue' column by removing dollar signs and commas\n",
    "gme_revenue['Revenue'] = gme_revenue['Revenue'].replace({'\\$': '', ',': ''}, regex=True)\n",
    "\n",
    "# Convert the 'Revenue' column to numeric format\n",
    "gme_revenue['Revenue'] = pd.to_numeric(gme_revenue['Revenue'], errors='coerce')\n",
    "\n",
    "# Display the cleaned DataFrame\n",
    "print(gme_revenue.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Display the last five rows of the `gme_revenue` dataframe using the `tail` function. Take a screenshot of the results.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    GameStop Annual Revenue (Millions of US $)  \\\n",
      "11                                        2009   \n",
      "12                                        2008   \n",
      "13                                        2007   \n",
      "14                                        2006   \n",
      "15                                        2005   \n",
      "\n",
      "   GameStop Annual Revenue (Millions of US $).1  \n",
      "11                                       $8,806  \n",
      "12                                       $7,094  \n",
      "13                                       $5,319  \n",
      "14                                       $3,092  \n",
      "15                                       $1,843  \n"
     ]
    }
   ],
   "source": [
    "# Display the last 5 rows of the gme_revenue DataFrame\n",
    "print(gme_revenue.tail())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 5: Plot Tesla Stock Graph\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `make_graph` function to graph the Tesla Stock Data, also provide a title for the graph. Note the graph will only show data upto June 2021.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Hint</summary>\n",
    "\n",
    "```\n",
    "\n",
    "You just need to invoke the make_graph function with the required parameter to print the graphs.The structure to call the `make_graph` function is `make_graph(tesla_data, tesla_revenue, 'Tesla')`.\n",
    "\n",
    "```\n",
    "    \n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA90AAAJNCAYAAAAs3xZxAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAACfzklEQVR4nOzdd3hTZePG8TvdlA4oowVkiUwFRFAooIAiUwVB3AgOVAQXrhdFBBfqz62IGxygvoqDLWU7GIKibBFBQCiblgJt0/b8/njeNEmbtmmbjrTfz3Xlylk5eZI+hd7nGcdmWZYlAAAAAADgcwFlXQAAAAAAACoqQjcAAAAAACWE0A0AAAAAQAkhdAMAAAAAUEII3QAAAAAAlBBCNwAAAAAAJYTQDQAAAABACSF0AwAAAABQQgjdAAAAAACUEEI3AFQC06ZNk81m07Rp08q6KGVq165dstlsGj58eFkXJVt5LNO3334rm82mn3/+uayLgkrs/fffV2BgoDZs2FDWRQGAYiF0A0ApsNlshXr4o7lz56p///6qXbu2goODVbNmTZ1zzjm65ZZb9N1337kdO2HCBNlsNi1btqxsCltMjvK7PqpWrao2bdpowoQJOnnyZFkXscjsdrsefvhh9e7dW507d87evmzZsgIvDnhzTHE4zj9hwoQSOb+D40JInz59SvR9SordbtfMmTM1bNgwtWzZUhEREYqMjFTHjh01ZcoUZWZm5vna6dOn64ILLlDVqlVVvXp1XXbZZfr1119zHffvv//q1VdfVa9evdSgQQOFhIQoLi5OgwcP1urVqz2ee/369Xr00UfVu3dv1apVSzabTd27d8+zLMOGDVPDhg310EMPFfo7AIDyJKisCwAAlcETTzyRa9urr76qpKQkj/v8zcSJEzVhwgSFh4frsssuU6NGjZSRkaFNmzbpiy++0J9//qkBAwaUdTF9bvDgwTrnnHMkSfv379esWbM0ceJEzZ49WytXrlRISEiB56hXr562bNmi6Ojoki6uVz755BNt375db7/9dlkXBUW0Y8cOXXXVVYqIiNAll1yiK664QklJSZo9e7buuusuzZs3T7Nmzcp1ge+ZZ57RuHHj1LBhQ9155506ceKEPv/8c3Xu3FmLFy9Wly5dso9944039Pzzz6tJkybq1auXatWqpe3bt+vbb7/Vt99+qxkzZuiaa65xO/+3336rSZMmKSQkRM2aNdPhw4fz/RzBwcG6//77dc899+inn35ye38A8CeEbgAoBZ5a5qZNm6akpKQSb7Urabt27dKTTz6p+vXra9WqVapbt67b/tOnT+fZ8uXvrrrqKl177bXZ6y+++KIuuOAC/frrr5oxY4ZXLb7BwcFq0aJFCZaycKZMmaL69eurR48eZV0UFFFkZKQmT56sYcOGqWrVqtnbX3rpJXXv3l1z5szRV199pSFDhmTv2759uyZMmKBmzZppzZo12ReB7rrrLnXq1EkjRozQxo0bFRBgOklecMEFWrZsmbp16+b23j/88IMuueQSjRw5UgMHDlRoaGj2viFDhuiKK65Q69atdeTIEdWpU6fAz3LttddqzJgxevvttwndAPwW3csBoJxJT0/Xyy+/rPPOO09Vq1ZVZGSkLrzwQs2aNSvXsUlJSRo/frxatWqliIgIRUVF6ayzztKwYcP0zz//FPhe33zzja677jqdddZZCg8PV3R0tC688ELNnDnT6/KuWbNGWVlZGjRoUK7ALUlVqlRx60LavXt3TZw4UZLUo0eP7O7ZjRo1cnvdxo0bdfXVV6t27doKDQ1V48aNdd999+nIkSMey3Hw4EE98MADat68uapUqaKYmBh17NhRL774YoGfIT09XVdffbVsNpsefvhhWZbl9ed3FRkZmR20f/nlF0nu4+lnz56tLl26KDIyMvvz5jem+8SJE5o4caLatGmT/fNp166dHn/8cdntdrdjd+7cqdtuu00NGjRQaGio6tSpo+HDh3tVDxw2btyotWvXavDgwT4d5tCoUSM1atRIx48f1x133KG4uDiFhYWpXbt2+uyzz7w6x4QJE7IvBEycONGta/+uXbuyjzt8+LDuu+8+NW7cWKGhoapdu7auvvpqbdy4sdifo3v37nl+L8OHD89VFtef/cKFC9W5c2eFh4erRo0aGjZsWJ51+Y8//tC1116rOnXqKCQkRA0bNtTdd9+d5/E51atXT3fddZdb4JakqlWrasyYMZKk5cuXu+2bOnWqMjIy9Nhjj7n1ujj33HN13XXXacuWLfrxxx+ztw8aNChX4JakCy+8UD169NCxY8dyjcU+++yzdd555yk4ONirzyFJtWrVUvfu3fXVV18pJSXF69cBQHlCSzcAlCNpaWnq06ePli1bpnPPPVe33nqr7Ha75s6dqwEDBuiNN97Q6NGjJUmWZal3795avXq1unTpoj59+iggIED//POPZs2apaFDh6phw4b5vt/YsWMVEhKirl27qk6dOjp06JBmzZqlq666Sq+//rruvvvuAstco0YNSaalzBuOcLl8+XINGzYsO3xWq1Yt+5gff/xRvXv3Vnp6uq666io1atRIK1eu1GuvvaY5c+Zo1apVqlmzZvbx27ZtU48ePbR//3517dpVAwcO1MmTJ7Vp0yY9++yzevDBB/Msz4kTJzRw4EAtXbpUL730UnYoKa6c4ezLL7/UwoULddlll+muu+5ScnJyvq8/ePCgunXrpq1bt+rcc8/VyJEjlZWVpa1bt+r555/XAw88kP2drV69Wr1799bJkyd12WWXqWnTptq1a5emT5+u+fPna+XKlTrzzDMLLPPixYslSZ06dSrah85Henq6evbsqZSUFA0dOlQnT57Uf//7X11//fU6fPhwgXWte/fu2rVrlz766CN169bN7UKO43s4dOiQ4uPjtWPHDnXv3l3XXnutdu7cqa+++kpz587V999/r65du/r8sxVk1qxZmjt3ri6//HJ17txZK1as0Mcff6wdO3a4BVnHsVdffbUCAgI0YMAA1a9fX5s3b9abb76p77//XqtXr1b16tWLXBZH4A0Kcv8T0DG/Qq9evXK9pnfv3po2bZqWL1+uiy66qMjvUVTx8fFatGiRfv75Z4/lA4ByzwIAlImGDRtaOf8ZfvTRRy1J1uOPP25lZWVlb09OTrY6dOhghYSEWP/++69lWZb1xx9/WJKsgQMH5jp3amqqdeLEiez1qVOnWpKsqVOnuh23Y8eOXK89ceKE1bp1ays6Oto6efJkgZ/jxIkTVoMGDSxJVv/+/a1PPvnE2rZtm1v5c3riiScsSdbSpUtz7cvMzLSaNGliSbIWLFjgtu+hhx6yJFm33HKL2/YOHTpYkqx333031/n27NmTvbxz505LkjVs2DDLsiwrMTHRateunRUcHGx98sknBX7WnOX/7LPP3LafOHHCatWqlSXJ+uijjyzLcn73AQEBVkJCQq5z5SyTw+DBgy1J1qOPPprrNYmJiZbdbrcsy7LS09OtRo0aWZGRkdavv/7qdtwPP/xgBQYGWpdddplXn2vIkCGWJGv79u259i1dutRjOb05xlHXL7roIistLS17+549e6yaNWtaoaGh1t69ewssn+P8TzzxhMf9N998syXJGjt2rNv2uXPnWpKss846y8rMzCzwfRw/k969e7tt79atW67fWYdhw4ZZkqydO3dmb3P87IOCgqwff/wxe3tGRobVvXt3S5K1cuXK7O2HDx+2oqKirHr16lm7du1yO/9nn31mSbJGjx5dYPnz07dvX0uSNXfuXLftNWvWtCIiIjy+Zu3atZYka+jQoQWe/59//rFCQ0OtOnXqWBkZGXket3//fkuS1a1btwLP+d1331mSrPHjxxd4LACUR3QvB4ByIisrS1OmTFGTJk2yu886REZGavz48UpPT9fXX3/t9roqVarkOldoaKgiIiIKfE9PrZ8REREaPny4kpKSsrtI5yciIkLffvutzj77bM2dO1dDhw5V8+bNVb16dV1++eX65ptvCjyHq59++kk7duxQ37591bt3b7d948ePV0xMjGbMmKH09HRJpnv72rVrddFFF2nEiBG5znfGGWd4fJ8dO3aoS5cu2rZtm2bNmqUbb7yxUOWUpK+++koTJkzQhAkTNHLkSDVv3lybN29Whw4d3MZ6S9KAAQPUs2dPr86bmJior7/+Wk2aNPE45j82Nja7FXHOnDnatWuXHnroIbVr187tuK5du2rAgAGaN29egS3rkrR3797s85eEZ5991m1yuTPOOEP33nuv0tLS9Pnnnxfr3Onp6frss89Uo0YNjRs3zm1fv379dOmll+qvv/7STz/9VKz3KYrrr7/ebTxyYGCghg0bJkluv2Mff/yxkpOTNWnSpFy9VK699lqdd955xfqe3n33Xc2fP18XX3yx+vXr57YvKSkpz8n8oqKiso/Jj91u19ChQ5WWlqbnn39egYGBRS6rK0d9dNRPAPA3dC8HgHJi27ZtOnbsmOrWrZs95tnVoUOHJElbt26VJLVs2VJt2rTRZ599pr1792rgwIHq3r27zj333OzJjgpy8OBBPffcc5o/f77++ecfnT592m3/vn37vDpPu3bttGHDBq1cuVJLly7VunXr9OOPP2rOnDmaM2eObrjhBn3yySdejRP+7bffJMnjrYQiIiLUoUMHLVy4UNu2bVPr1q21Zs0aSZ67xeZl69at6tKlizIyMrRkyRJ17NjR69e6mjlzZvb49/DwcDVp0kS33367HnzwwVwzl19wwQVen3ft2rWyLEs9evQocPzrqlWrJJn64ymgJyYmKisrS3/++ac6dOiQ77mOHDmiwMBARUZGel1WbwUFBSk+Pj7X9gsvvFCS8+deVFu3blVqaqp69Oih8PDwXPt79OihhIQErV+/Pvs9S0v79u1zbXNcDDp+/Hj2NsfPcvXq1dqxY0eu16Smpurw4cM6fPiw2/AKb8yZM0ejR49Ww4YN9emnnxbqtd7IysrS8OHDtWLFCo0YMUJDhw712bljYmIkqcDZzgGgvCJ0A0A5cfToUUnSpk2btGnTpjyPc9wDOigoSEuWLNGECRM0c+ZMPfDAA5LMxEOjR4/WY489lm9L09GjR3X++edr9+7d6tKli3r27Klq1aopMDBQ69ev13fffae0tDSvy2+z2dS5c+fseztblqXvvvtON910k6ZPn67BgwfryiuvLPA8jhbZvFpbHTMeO45ztL7Vq1fP67L++eefOnbsmDp37px9y6+i+Oyzz3K1aOelMK3HhflMjnozffr0fI/z5t7hVapUUWZmpux2e66w77iQk5WVlefrHfs8XfSpWbOmx+2O76WgVtSCFLbelCZHS7ErR08F13tmO36WkydPzvd8J0+eLFTonjdvnq666irFxsZqyZIlHmcNj46OzvNn4PjO8moJz8rK0i233KIZM2boxhtv9Pnt5hwXAz1dTAEAf0D3cgAoJxx/mA8ePFiWZeX5mDp1avZratSooTfeeEP//vtv9mRLMTExeuKJJ/TCCy/k+34ffPCBdu/eraeeeko//vij3njjDT311FOaMGGCTybSstlsGjhwoO6//35J0pIlS7x6neN7OHDggMf9iYmJbsc5JtH6999/vS7bFVdcoQkTJujnn39Wv379vAqkxVWY2cAL85kc38Ps2bPzrTeeZprOqVatWpKc4c+VI3DlN4O2oyXSUzg7fPiwx8Du+DkX9z7lha03ReG4aJCRkZFrX3EvGkjOsm3YsCHfn2VBEyS6mjt3rgYNGqSaNWtq6dKleU6o17RpU6WkpGR/T64ckyQ2bdo0176srCzdfPPN+uijj3Tddddp2rRpXve08ZajPjrqJwD4G0I3AJQTLVu2VFRUlNauXZvrdlAFsdlsatmypUaNGqWEhARJ8niLMVeO7qsDBgzIte+HH34o1Pvnx9PYckcLvGsrn4NjXLJjNmVXJ0+e1Nq1a1WlShU1b95ckrPb9sKFCwtVrieeeEJPPfWUVqxYob59+5ar2xF16NBBAQEBWrp0aYF1wdE1fuXKlcV+39atW0syXdVzat68uUJCQvTLL794DJ2uZWjTpk2ufRkZGR7L6KhrOceje5JfvWnRooXCwsL0yy+/6NSpU7n2O+rTueeeW+D75MUxa3jOiyFZWVn6/fffi3xeB1/+LCUTuAcPHqyYmBgtXbpUZ511Vp7HOi7KePo9+v77792OcXAE7o8//ljXXHONPvnkE5+N43blqI+O+gkA/obQDQDlRFBQkEaOHKl//vlHDz74oMewtXHjRh08eFCSub+z6z2BHRwtfWFhYfm+n6O1LOcti2bMmKF58+Z5Xe41a9bo448/Vmpqaq59hw4d0vvvvy9JbrdqcozR3LNnT67XdOnSRU2aNNH8+fO1aNEit31PP/20jhw5ouuuuy57zPT555+v888/XytWrNB7772X63z5tRaPGzdOzzzzjH744YdyFbxjY2M1ePBg7dixw+P4/oMHD2YH3wEDBqhBgwZ6+eWXtWLFilzH2u32XD/jvDhC1erVq3PtCwsL09VXX61Dhw7p6aefzrV/w4YNev/99xUZGZnnMIJHH300ewI8yUyM9dprryk0NNSrbvr51ZuQkBBdd911Onz4sCZNmuS2b8GCBfr+++911llnuU1oVljnn3++JHP/bVcvv/yydu7cWeTzOtx8882KjIzUY4895nGIyalTp7LHfRdk/vz5Gjx4sKpXr66lS5d6bKXO+d5BQUF65pln3Frt169fr88++0wtW7Z0+x12dCn/+OOPNWTIEH366aclErglZ330prcGAJRHjOkGgHJk4sSJ+vXXX/X6669r7ty5uuiii1S7dm39+++/2rBhg37//XetXLlStWvX1vr16zVo0CBdcMEFatWqleLi4vTvv//q22+/VUBAQHa37rwMHTpUzz//vO6++24tXbpUDRs21O+//67Fixdr0KBBuWZJz8u+ffs0bNgwjR49WhdddJFatGihoKAg/fPPP5ozZ45SUlLUv39/DRkyJPs1PXr0kM1m06OPPqpNmzYpOjpa1apV0+jRoxUQEKBp06apd+/e6tevn4YMGaKGDRtq5cqVWrZsmZo0aaLnnnvOrQzTp09X9+7ddfvtt+uTTz5RfHy8UlNTtWnTJv3222/5dol+9NFHFRAQoLFjx6pPnz5asGCBVzO/l7S33npLGzdu1DPPPKN58+bp4osvlmVZ+vPPP7Vw4UIdOHBA1apVU2hoqL766iv17dtX3bp108UXX6zWrVvLZrPpn3/+0Q8//KAaNWpkT8CXn0suuUSRkZFKSEjQQw89lGv/Sy+9pNWrV2vixImaM2eOunXrprCwMP3555+aNWuWLMvS9OnT3e657lCnTh2dPHlSbdq00eWXX559n+4jR47o9ddf92r8eosWLVS3bl19/vnnCg0N1RlnnCGbzaa7775b0dHRev7557V8+XI9/fTT+vnnn9WxY0ft2rVLX375pcLDwzV16tRidX2++eab9cILL2jChAlav369mjRporVr12rjxo3q1q2bli9fXuRzS6b79GeffaYhQ4aobdu26tOnj1q0aKG0tDTt2rVLy5cvV+fOnbVgwYJ8z7N161ZdeeWVSktLU/fu3fXZZ5/lOqZRo0YaPnx49nqzZs00YcIEjRs3Tm3bttXgwYN14sSJ7NnS33vvPbfv7sknn9RHH32kiIgINWvWzOOFmIEDB7r1LNi6dWv2765jnPbWrVvdypHzgoZlWVq8eLFatmypZs2a5fu5AaDcKq17kwEA3Hm6T7dlmXv4vvPOO1aXLl2sqKgoKzQ01GrQoIHVp08fa8qUKVZKSoplWeYex//5z3+sTp06WbVr17ZCQkKsBg0aWIMGDXK7969l5X2f7vXr11u9evWyqlevbkVGRlrdunWzFi1alOfxniQnJ1uffvqpNXToUOvss8+2qlWrZgUFBVm1atWyLrnkEuuDDz7weL/eadOmWa1bt7ZCQ0MtSVbDhg3d9v/xxx/WVVddZdWsWdMKDg62GjZsaN17773WoUOHPJYjMTHRuvfee60zzzzTCgkJsWJiYqyOHTtaL7/8cvYxed0T27Is6/nnn7ckWZ07d7aSk5Pz/cx53afbk4K+y/zKlJSUZD3++ONWixYtrNDQUCs6Oto699xzrfHjx1vp6elux+7du9e69957raZNm1qhoaFWVFSU1bJlS+u2226zFi9eXGA5HUaOHGkFBgZa+/bt87j/+PHj1hNPPGG1bdvWqlq1qhUcHGzVr1/fuv7663PdJ9yhYcOGVsOGDa2jR49at99+uxUbG2uFhoZabdu2tWbMmOF12SzLslatWmV169bNioyMtCTlujf2oUOHrHvuucdq2LChFRwcbNWsWdO66qqrrA0bNnj9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dKm+++473X333V6Vr379+mrSpInHwO2NNm3a5HkbvHbt2ikzM1MHDx7M9TPJbwZ+AAAAQJIyM6Wvv5b27TPrI0ZI27dLjFIsO7R0V3ITJ07UPffco+joaPXp00dpaWlau3atjh07pjFjxujll19WnTp11K5dOwUEBOjLL79UXFycx8DZtGlT7d69W59//rnOP/98zZ07V998802+7//OO+9o/fr1uvLKK9WkSROlpqbq448/1qZNm/TGG29IMmPDU1JStHjxYrVt21bh4eFq2rSpBgwYoBEjRuidd95RZGSk/vOf/6hevXoaMGCAJDMxX+vWrXXXXXfpzjvvVEhIiJYuXaohQ4aoZs2a2WVo1qyZli5dqu7duysoKEivvvqqz75fTx5//HFdeumlmjBhgq677jplZGRo3rx52TO/33DDDbrpppuyJ2M7dOiQFi9erDZt2qh///4lWjYAAAD4t/ffl+680wxF/V8bliQpLKzsylTZ0dJdyd122216//33NXXqVLVu3VrdunXTtGnTslu6IyMjsyckO//887Vr1y7NmzfP4/2lr7jiCt1///0aPXq0zj33XP388896/PHH833/Cy64QCkpKbrzzjt19tlnq1u3blq1apW+/fbb7EnNOnfurDvvvFPXXHONatWqpRdeeEGSNHXqVLVv316XXXaZ4uPjZVmW5s2bl33vxmbNmmnhwoX6/fffdcEFFyg+Pl7fffedgoJyX2tq3ry5lixZos8++0wPPPBAsb7TgnTv3l3Tpk3T7Nmzde655+riiy92u7/81KlTddNNN+mBBx5Q8+bNNXDgQP3yyy9q0KBBiZYLAAAA/m/BAvN86pT79hK6mRO8YLMsb+/2XHkkJycrOjpaSUlJioqKkt1u17x589SvXz9lZmZq586daty4scK4XIQiyMrKUnJysqKiojxevCis1NRU6mQl5vrvk+OCE1BU1Cf4EvUJvkR98t5VV0kzZ5plyzJzUEnSAw9IL75YduUqT1zr0+nTp92yX0mgpRsAAAAAKgjXuXjtdufySy9J775b+uUBoRsAAAAAKgzX0J2zi/kdd5RuWWAQugEAAACggnAN3adPl1054EToBgAAAIAKgtBd/hC6i4j551BeZGVllXURAAAAUE4UFLqPHSu9ssDgPt2FFBwcLJvNpkOHDqlWrVqyOaYDBLyUlZWl9PR0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SZKwc+dOODg4NHhcq9Uq/hqIiIjsFZtuIiKiFi4nJwcAEBcXh4qKCuzZswc6nQ7p6enyOsXFxQ1+T5KkRrfXo0cPCCHg6+uLgICA5imaiIioheA13URERC1Yfn4+9Ho9fH198dRTT8lnpi2zlFusXLmywe86OzsDQIPZyBMTE+Hg4ACdTtdgO0KIerceIyIiau14ppuIiKiF2LlzJ3755RcYjUb8+eefyM/Px+7du+Hj44Pt27dDo9FAo9EgJiYGS5cuRW1tLbp27Ypdu3bBYDA02F5ERAQAYOHChUhKSoJarUZCQgJ69OiBjIwMzJ8/H7/++ivGjBkDFxcXGAwGfP7555gxYwbmzJnzX798IiIim8Smm4iIqIWwDBd3cnKCu7s7goODsXLlSkydOhUuLi7yeps2bUJqaireffddCCEwbNgw7Ny5E126dKm3vb59+0Kv12PdunX4+uuvYTabYTAY4OzsjFdffRUBAQFYsWIFdDodAMDb2xvDhg3D6NGj/7sXTUREZOMk8c9xYURERERERESkCF7TTURERERERNRM2HQTERERERERNRM23URERERERETNhE03ERERERERUTNh001ERERERETUTNh0ExERERERETUTNt1EREREREREzYRNNxEREREREVEzYdNNRERERERE1EzYdBMRERERERE1EzbdRERERERERM2ETTcRERERERFRM/kfoG/egJd9aeEAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Fetch Tesla stock data using yfinance\n",
    "tesla = yf.Ticker(\"TSLA\")\n",
    "\n",
    "# Get historical data up to the maximum period\n",
    "tesla_data = tesla.history(period=\"max\")\n",
    "\n",
    "# Filter data up to June 2021 (end of June 30, 2021)\n",
    "tesla_data = tesla_data[tesla_data.index <= '2021-06-30']\n",
    "\n",
    "# Define a function to create the graph\n",
    "def make_graph(data):\n",
    "    # Plot the 'Close' price of Tesla stock\n",
    "    plt.figure(figsize=(10,6))\n",
    "    plt.plot(data.index, data['Close'], label='Tesla Stock Price', color='blue')\n",
    "\n",
    "    # Add labels and title\n",
    "    plt.title('Tesla Stock Price (Up to June 2021)', fontsize=14)\n",
    "    plt.xlabel('Date', fontsize=12)\n",
    "    plt.ylabel('Price (USD)', fontsize=12)\n",
    "\n",
    "    # Rotate the x-axis labels for better readability\n",
    "    plt.xticks(rotation=45)\n",
    "    \n",
    "    # Show grid\n",
    "    plt.grid(True)\n",
    "\n",
    "    # Display the legend\n",
    "    plt.legend()\n",
    "\n",
    "    # Show the plot\n",
    "    plt.tight_layout()  # Adjust the layout to prevent clipping\n",
    "    plt.show()\n",
    "\n",
    "# Call the function to create the graph\n",
    "make_graph(tesla_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 6: Plot GameStop Stock Graph\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `make_graph` function to graph the GameStop Stock Data, also provide a title for the graph. The structure to call the `make_graph` function is `make_graph(gme_data, gme_revenue, 'GameStop')`. Note the graph will only show data upto June 2021.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Hint</summary>\n",
    "\n",
    "```\n",
    "\n",
    "You just need to invoke the make_graph function with the required parameter to print the graphs.The structure to call the `make_graph` function is `make_graph(gme_data, gme_revenue, 'GameStop')`\n",
    "\n",
    "```\n",
    "    \n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA90AAAJNCAYAAAAs3xZxAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAACjfUlEQVR4nOzdd3gUVdvH8d+mJ5BC7733roJIL4o0AbEgTVSkiIDKIypVBLEAAoJiAcUCdlR6FaQXpUiH0HtLgJC68/6Rd5csu5tskg2bhO/nubyenTNnZu/ZnYTcc5rJMAxDAAAAAADA7bw8HQAAAAAAANkVSTcAAAAAABmEpBsAAAAAgAxC0g0AAAAAQAYh6QYAAAAAIIOQdAMAAAAAkEFIugEAAAAAyCAk3QAAAAAAZBCSbgAAAAAAMghJNwAAd4HJZFKTJk08HYaNzBbTP//8I29vb3333XeeDgX3sBUrVshkMmnRokWeDgVANkHSDQAO/Pvvv3rxxRdVuXJlhYSEyM/PTwULFlTLli314Ycf6uLFi54OMV0uX76s119/XVWqVFFQUJCCgoJUokQJNW/eXGPGjNH58+dt6me25Cyp9evX6/HHH1eRIkXk5+enXLlyqWLFinr66af11Vdf2dSdM2eOTCaT5syZ45lg08kSf9L/AgMDVbFiRQ0dOlSXLl3ydIjpMnToUFWsWFFPPvmktezYsWMp3n+u1EkPy/l79eqVIedPymQyqWLFihn+PhnBMAwtXrxY/fr1U/Xq1RUaGqqgoCDVqFFD48ePV3R0tNNjly5dqsaNGys4OFghISFq2rSpVq5caVfv8uXLmjVrltq3b6/SpUvL399fefPm1SOPPKKlS5c6PPeRI0c0evRotW/fXkWKFJHJZFLJkiWdxtKiRQs1bNhQw4YNU0JCQqo/BwC4k4+nAwCAzMRsNmvYsGH68MMP5e3trUaNGqlVq1bKkSOHLly4oI0bN+rVV1/VqFGjdODAARUpUsTTIafaqVOn1KBBA508eVI1a9ZU7969FRYWprNnz2rDhg0aPXq0HnzwQRUoUMDToaZozpw5evbZZ+Xj46M2bdqoXLlyMplMOnDggBYtWqS1a9eqZ8+eng7T7Zo3b66GDRtKki5evKilS5dq8uTJ+uWXX7R9+3blyZPHpfPs27dPQUFBGRmqy1atWqU1a9boiy++kJcXbQJZUUxMjNq0aSN/f381adJErVu3VnR0tJYuXao333xTv/32m9asWWN3z33zzTfq3r278uXLZ32wMX/+fLVs2VI//PCDunTpYq37448/ql+/fipcuLCaN2+uIkWK6NSpU/r555+1ZMkSvffee3rttddszr9u3TqNGTNG3t7eqlSpks6dO5fitQwbNkzt27fXvHnz1K1bt/R/OADubQYAwOr11183JBm1a9c2Dh065LDO9u3bjRYtWjjdn9k9++yzhiRj7NixDvfv2rXLOHHihE2ZJKNx48Z3ITrX3bx50wgODjZCQkKMPXv22O2PjY01li1bZlM2e/ZsQ5Ixe/bsuxTlbe74DC3xT5gwwaY8NjbWaNq0qSHJGDVqVLrew1O6dOliBAYGGhERETbl4eHhKX52rtRJD8v5e/bsmSHnT0qSUaFChQx/n4wQGxtrjBs3zrhy5Ypdebt27QxJxnvvvWez78qVK0ZYWJiRN29e4+TJk9bykydPGnnz5jXy5s1rREZGWstXrlxp/P7770ZCQoLNefbv32+EhoYavr6+xunTp232HTlyxNi4caMRFRVlGIZh+Pv7GyVKlEjxWvLmzWs0bNjQ5esHAGd4lAwA/+/gwYN6//33lS9fPi1ZskRly5Z1WK927dpavny5XffEL7/8Uh06dFDJkiUVEBCg3Llzq3Xr1lq9erXdOdasWSOTyaTRo0drw4YNatq0qYKDg5UvXz71799ft27dkiQtXLhQ9evXV44cOVSgQAENGzZM8fHxDuNasGCBmjdvrly5cikgIEBVq1bVBx98YNc9cuPGjZKkl156yeF5qlWrpmLFitnEKUl//fWXTbfmpF204+PjNWnSJNWoUUOBgYEKDQ1V06ZN9ccff9idP2kX7wULFui+++5TUFCQ8uXLp2effdaua7sze/bs0fXr19W0aVNVqVLFbr+vr69atmxp3e7Vq5d69+4tSerdu7fNtSR1/Phx9enTx9pdvWjRourTp49OnDjhMI7r169rzJgxql69uoKCghQaGqpatWppxIgRiouLS/YaDMPQkCFDZDKZ1K1btxTrO+Pr66u+fftKkrZu3SrJ/h5r1aqVwsLCbK7XWZfs2NhYTZ48WfXq1VNwcLBy5sypypUra+jQobp69apN3QsXLmjIkCEqW7astatv586dtWfPHpfjv3r1qhYsWKDWrVsrJCQkDZ+AY02aNJHJZFJ0dLRef/11FS9eXAEBAapUqZKmTZsmwzBSPMecOXNUqlQpSdJXX31lc9+sWbPGWu/mzZsaNWqUKlasaP35f/TRR7V+/fp0X0evXr1kMpl07Ngxu32jR4+2iyXpd79t2za1bNlSwcHBCg0N1WOPPebwPJIUHh6u5557TsWLF5e/v78KFSqkXr166fjx4y7F6evrqzfffFO5cuWyKx8+fLikxN8jSf3444+6du2aXnrpJRUtWtRaXrRoUQ0cOFCXLl3Sr7/+ai1v1qyZ2rVrZ9cbokKFCnriiScUFxenDRs22OwrXbq0HnjgAQUGBrp0HZaYO3bsqL///luHDx92+TgAcISkGwD+31dffaWEhAT17dtX+fLlS7G+j4/tCJ0BAwbo/PnzatGihYYMGaK2bdtq48aNatGihRYsWODwHJs3b1bz5s0VGhqqvn37qnjx4po5c6aef/55zZ8/X126dFGJEiXUt29fhYWF6f3339f48ePtzjN8+HB17NhRBw4cUKdOndS/f38FBgbqtddesxkfK8na9fjgwYMpXmPJkiU1atQoSVKJEiU0atQo6381a9aUlJg4dunSRa+88oqio6M1YMAAPf3009q5c6fat2+vyZMnOzz3zz//rMcff1xly5bV4MGDVa1aNc2ePVsNGza0S+wcsVzH0aNHXRp32bFjR3Xo0EGS1KFDB5trsTh48KDq1aunL7/8UnXq1NErr7yiWrVq6csvv1TdunXtPrMLFy7ovvvu0+jRo+Xt7a1+/frp2WefVcGCBTVx4kTdvHnTaTxxcXF65plnNGXKFA0ePFjffPONfH19U7yOlNz5EGHDhg3W5POFF17QE088kezxt27dUrNmzTR06FBFRESod+/e6tevn8qXL69PP/3UJgE7cuSI6tSpoylTpqhMmTJ66aWX1KZNGy1ZskQPPPCANm/e7FLMa9euVVxcnB544IHUX7ALunbtqm+//VadOnXSiy++qBs3bmjQoEF69dVXUzy2Zs2aevnllyVJNWrUsLlvLA/eoqOj1axZM40dO1Y5cuTQ4MGD1aFDB61evVqNGzfWjz/+mCHXlZKtW7eqUaNG8vPzU9++fVW3bl399ttvatGihd346s2bN6tWrVr66quvVKdOHb388st66KGH9O233+q+++7T0aNH0xWL5d6+8/em5WFBq1at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Q5vrsMR2p+LFi6tp06b677//7MbHz5o1S/v27VOzZs2sXekLFCigzp0768iRIw679l+4cMHpmuo9evTQnDlzdODAATVp0sTaGuppPj4+6tu3ryIiIvTyyy/bJZkRERG6ceOGJOm+++7T/fffr++//17z58+3O5fZbHZ5qSdLUuVsibGePXsqPj5er732mt0DkVOnTun999+Xt7e3w/tMkt5++22bFuGIiAiNGzdOJpPJpZb4XLlyyWQyObxvLPHFxcVp+PDhNvHt2rVLc+bMUWhoqDp27Jji+zhjaSWeM2eOTflPP/3k8mecnA4dOqh48eKaNGmS9eFSUnFxcXa/25zZvn27WrZsqfj4eC1evNi67JYzXbt2VWhoqKZNm2bzO+bUqVOaPn268ubNq8cee8zmmJEjR2rcuHF66KGHMizhlm7fj6lp4QcARxjTDQBJvPPOO4qNjdWkSZNUsWJFNWrUSDVq1FBQUJAuXLigXbt2acuWLdYJvyxefPFFzZ49W507d1bXrl2VJ08ebdq0STt27NCjjz6a7JjX9Hr44Yc1YsQIvf322ypbtqwefvhhlShRQpcvX9bhw4e1bt06jRs3TpUqVZIkzZ07V6+++qqqVaum+++/X/nz59e1a9es8QYGBmrmzJk279GsWTP98MMP6tixo2rVqiVvb2+1b99e1atXV/fu3fXLL79owYIFql69utq2baubN29q/vz5unLlij788EOHrdZt27ZVu3bt1KVLF5UsWVKbNm3S6tWrVaZMGY0dOzbF646IiNBLL72k1157TQ0bNlTVqlUVGBio06dPa+HChbp8+bLq1Kmjl156yXpM/fr1FRgYqClTpujq1avWbqNvvfWWJGnmzJlq2LChnn/+ef3xxx+qXLmy/vvvP/3+++/Kly+f3ecyY8YM7dmzR++8844WLVqkZs2ayTAMHTx4UMuWLdP58+edTg7WvXt3eXl5qWfPnmrSpIlWr15tHf/rSWPHjtWmTZs0d+5cbdq0SY888oj8/f119OhRLVmyRH///bf13v/+++/VtGlTPfnkk5oyZYpq166twMBAnThxQhs3btTFixcdjtO+U/Xq1VW6dGktX77c4f433nhDK1as0OzZs7Vx40a1bNlSISEhOn78uBYsWKAbN27oww8/VPny5R0eX758eVWtWlWdO3eWlLhG/KlTpzR06FCX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fbvMZrM+/PBDPfDAAypfvrzOnDmT7hhq1aqlhIQEXbhwQWXLlrX5L2nX7DtVrlxZkqxx+/n52UzOJkmVKlXSzp07ba5t/fr18vLysulSv3PnTt26dcu6vWnTJuXMmVNFixZ1+TrcEU9wcLBKliyplStXJvte7du313fffafnnntO8+bNSzE2Ly8vlS1bVqVLl3Y5sU+qXLlyCgwMdBpX7dq1dejQIeXPn9/uO2QWdAAAALji293fatmRZdp3aZ+nQ8lUSLqzgRkzZig+Pl5169bV/PnztW/fPh04cEDffPON9u/fb219Llu2rOLi4jRt2jQdPXpUc+fO1SeffJLu9y9fvry6deumHj166JdfflF4eLi2bNmiCRMmaOHChZKkfv366e2339b69et1/Phxbdq0ST169FC+fPlUv359SYljzHft2qUDBw7o0qVLiouLU7du3RQQEKCePXtqz549Wr16tV566SV1797d2rVckmJjY9WnTx/t3btXixYt0qhRozRgwACn3cQzMp7Ro0frww8/1NSpU3Xo0CHt2LFD06ZNs4vhscce09y5c9W7d2/99NNP6f4ekhMQEKD//e9/GjZsmL7++msdOXJEmzZt0hdffCFJ6tatm/LmzasOHTpo3bp1Cg8P15o1azRo0CCdOnUqQ2MDAABA9pKalZjuBSTd2UCZMmX0zz//qEWLFho+fLhq1KihunXratq0aXr11Vf19ttvS0oc9zxp0iRNnDhRVatW1bfffqsJEya4JYbZs2erR48eeuWVV1ShQgV17NhRW7duVfHixSVJLVq00KZNm/T444+rfPny6ty5swICArRy5UrruO/nn39eFSpUUN26dZUvXz6tX79eQUFBWrp0qa5cuaJ69eqpS5cuat68uaZPn27z/s2bN1e5cuXUqFEjPfHEE2rfvr1GjRrlNN6MjKdnz56aMmWKZsyYoSpVqqht27Y6dOiQwzi6dOmir776St27d9cvv/ySru8gJSNGjNArr7yikSNHqlKlSnriiSes4/KDgoK0du1aFS9eXJ06dVKlSpXUp08fRUdHKyQkJEPjAgAAALIzk3GPPYaIjIxUaGioIiIi7JKJ6OhohYeHq1SpUgoICPBQhEitXr166dq1a/rtt99sys1msyIjIxUSEuK0xRtpx8+Le8XFxWnRokVq06aN3RwKQGbEPYushPsV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29d5+eWXycjIsM/4qJ2VOJMyK0aivIrRKLNiJMqrXKLh5WIIZrMZm81m3xFdOkM4efJk0tPT+frrrzXZhNQqyqwYifIqRqPMipEor6Ir3WIYl+b8c3d3JyIigpkzZ/LKK6/w3//+l3bt2jm5OpGalFkxEuVVjEaZFSNRXl2bTqmIYVw6K+jh4cGSJUsIDAxk27ZtdOzY0cmViVyZMitGoryK0SizYiTKq2vTlW4xnPj4eACysrKIjY11cjUi16bMipEor2I0yqwYifLqmvScbjGkc+fO4efn5+wyRK6bMitGoryK0SizYiTKq+tR0y0iIiIiIiLiIBpeLiIiIiIiIuIgarpFREREREREHERNt4iIiIiIiIiDqOkWERERERERcRA13SIiIiIiIiIOoqZbRERERERExEHUdIuIiIiIiIg4iJpuERGR28jSpUsxmUz2f97e3oSHhxMfH8+8efMoLS39RdvNysoiNTWV06dP39yCRUREbnNqukVERG5DU6dOZdmyZSxatIgnn3wSgKeffpqoqCiys7NveHtZWVmkpaWp6RYREblB7s4uQERERG6+3//+98TGxtpfT5o0iU2bNjFgwAAGDhxIbm4uPj4+TqxQRETENehKt4iIiIvo06cPL774IocPH2b58uUAZGdn8/DDD9OsWTO8vb0JCwvjkUceoaioyP6+1NRUnnnmGQCaNm1qH7p+6NAh+zrLly8nJiYGHx8fgoKCSEpKoqCg4JZ+PhERkdpITbeIiIgLeeihhwDYsGEDABs3buTAgQOkpKQwf/58kpKSWLlyJf3798dmswGQmJjI0KFDAZgzZw7Lli1j2bJlBAcHA/DSSy8xYsQIWrZsyezZs3n66afJzMykV69eGo4uIiIuT8PLRUREXEijRo2oU6cO+fn5ADz++OOMHz++2jpdu3Zl6NChbNu2jZ49exIdHU3Hjh1ZsWIFCQkJNGnSxL7u4cOHmTJlCunp6Tz33HP25YmJiXTo0IGFCxdWWy4iIuJqdKVbRETExfj7+9tnMb/8vu6ysjJOnjxJ165dAfjqq6+uua0PPvgAq9XK4MGDOXnypP1fWFgYLVu25NNPP3XMhxARETEIXekWERFxMWfPniUkJASA4uJi0tLSWLlyJcePH6+23pkzZ665rby8PGw2Gy1btrzi1z08PH59wSIiIgampltERMSFHDlyhDNnztCiRQsABg8eTFZWFs888wzt27fH398fq9VKv379sFqt19ye1WrFZDKxbt063Nzcanzd39//pn8GERERI1HTLSIi4kKWLVsGQHx8PKdOnSIzM5O0tDQmT55sXycvL6/G+0wm0xW317x5c2w2G02bNiUyMtIxRYuIiBiY7ukWERFxEZs2bWLatGk0bdqU4cOH269MX5ql/JK5c+fWeK+fnx9AjdnIExMTcXNzIy0trcZ2bDZbtUePiYiIuCJd6RYREbkNrVu3jj179lBRUUFhYSGbNm1i48aNNG7cmH/96194e3vj7e1Nr169eOWVV7BYLDRs2JANGzZw8ODBGtuLiYkB4PnnnycpKQkPDw/uv/9+mjdvTnp6OpMmTeLQoUMkJCQQEBDAwYMH+fDDDxk9ejQTJky41R9fRESk1lDTLSIichu6NFzc09OToKAgoqKimDt3LikpKQQEBNjXe++993jyySd5/fXXsdlsxMXFsW7dOsLDw6ttr1OnTkybNo3Fixezfv16rFYrBw8exM/Pj2effZbIyEjmzJlDWloaABEREcTFxTFw4MBb96FFRERqIZPtp2PBREREREREROSm0D3dIiIiIiIiIg6ipltERERERETEQdR0i4iIiIiIiDiImm4RERERERERB1HTLSIiIiIiIuIgarpFREREREREHERNt4iIiIiIiIiDqOkWERERERERcRA13SIiIiIiIiIOoqZbRERERERExEHUdIuIiIiIiIg4iJpuEREREREREQf5f3LcDWXrre4lAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Fetch GameStop stock data using yfinance\n",
    "gamestop = yf.Ticker(\"GME\")\n",
    "\n",
    "# Get historical data for GameStop up to the maximum period\n",
    "gme_data = gamestop.history(period=\"max\")\n",
    "\n",
    "# Filter data up to June 2021 (end of June 30, 2021)\n",
    "gme_data = gme_data[gme_data.index <= '2021-06-30']\n",
    "\n",
    "# Fetch revenue data (as per the earlier instructions, assuming gme_revenue DataFrame exists)\n",
    "# Note: Ensure gme_revenue is already cleaned and contains the 'Date' and 'Revenue' columns\n",
    "\n",
    "# Define the make_graph function\n",
    "def make_graph(stock_data, revenue_data, stock_name):\n",
    "    # Plot the 'Close' price of the stock\n",
    "    plt.figure(figsize=(10,6))\n",
    "    plt.plot(stock_data.index, stock_data['Close'], label=f'{stock_name} Stock Price', color='green')\n",
    "\n",
    "    # Add title and labels\n",
    "    plt.title(f'{stock_name} Stock Price (Up to June 2021)', fontsize=14)\n",
    "    plt.xlabel('Date', fontsize=12)\n",
    "    plt.ylabel('Price (USD)', fontsize=12)\n",
    "\n",
    "    # Rotate the x-axis labels for better readability\n",
    "    plt.xticks(rotation=45)\n",
    "\n",
    "    # Show grid for better readability\n",
    "    plt.grid(True)\n",
    "\n",
    "    # Display the legend\n",
    "    plt.legend()\n",
    "\n",
    "    # Show the plot\n",
    "    plt.tight_layout()  # Adjust layout to prevent clipping\n",
    "    plt.show()\n",
    "\n",
    "# Call the function to plot GameStop data\n",
    "make_graph(gme_data, None, 'GameStop')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2>About the Authors:</h2> \n",
    "\n",
    "<a href=\"https://www.linkedin.com/in/joseph-s-50398b136/\">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.\n",
    "\n",
    "Azim Hirjani\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Change Log\n",
    "\n",
    "| Date (YYYY-MM-DD) | Version | Changed By    | Change Description        |\n",
    "| ----------------- | ------- | ------------- | ------------------------- |\n",
    "| 2022-02-28        | 1.2     | Lakshmi Holla | Changed the URL of GameStop |\n",
    "| 2020-11-10        | 1.1     | Malika Singla | Deleted the Optional part |\n",
    "| 2020-08-27        | 1.0     | Malika Singla | Added lab to GitLab       |\n",
    "\n",
    "<hr>\n",
    "\n",
    "## <h3 align=\"center\"> © IBM Corporation 2020. All rights reserved. <h3/>\n",
    "\n",
    "<p>\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  },
  "prev_pub_hash": "83a07babb305ceb42e09cd85ba8721036292c63a89e4dfdc9f0eaa89fb9cd33d"
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
