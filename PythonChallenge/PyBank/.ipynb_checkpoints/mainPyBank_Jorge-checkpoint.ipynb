{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 391,
   "metadata": {},
   "outputs": [],
   "source": [
    "# -*- coding: utf-8 -*-\n",
    "\"\"\"\n",
    "Created on Wed Oct  2 21:50:07 2019\n",
    "\n",
    "@author: yorch\n",
    "\"\"\"\n",
    "\n",
    "# -*- coding: UTF-8 -*-\n",
    "\"\"\"PyBank Homework Solution.\"\"\"\n",
    "\n",
    "# Dependencies\n",
    "import csv\n",
    "import os\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 401,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Files to load and output (Remember to change these)\n",
    "file_to_load = os.path.join(\"Resources\", \"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 402,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jan-2010</td>\n",
       "      <td>867884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Feb-2010</td>\n",
       "      <td>984655</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mar-2010</td>\n",
       "      <td>322013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apr-2010</td>\n",
       "      <td>-69417</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May-2010</td>\n",
       "      <td>310503</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Date  Profit/Losses\n",
       "0  Jan-2010         867884\n",
       "1  Feb-2010         984655\n",
       "2  Mar-2010         322013\n",
       "3  Apr-2010         -69417\n",
       "4  May-2010         310503"
      ]
     },
     "execution_count": 402,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Import the books.csv file as a DataFrame\n",
    "file_to_load_df = pd.read_csv(file_to_load)\n",
    "file_to_load_df.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 403,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Determine Rows Count\n",
    "rows_count = len(file_to_load_df[\"Date\"].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 404,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'$ 38,382,578'"
      ]
     },
     "execution_count": 404,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Determine Sum\n",
    "sum_gl = file_to_load_df[\"Profit/Losses\"].sum()\n",
    "sum_gl = ((\"$ {:,}\".format(sum_gl)))\n",
    "sum_gl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 405,
   "metadata": {},
   "outputs": [],
   "source": [
    "change = file_to_load_df[\"Profit/Losses\"].diff()\n",
    "file_to_load_df[\"ChangeinProfits\"] = change\n",
    "average = file_to_load_df[\"ChangeinProfits\"].mean()\n",
    "average = ((\"$ {:.0f}\".format(average)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 406,
   "metadata": {},
   "outputs": [],
   "source": [
    "greatest_increase_num = file_to_load_df[\"ChangeinProfits\"].max()\n",
    "greatest_date = file_to_load_df.loc[file_to_load_df[\"ChangeinProfits\"] == greatest_increase_num]\n",
    "greatest_date = greatest_date[\"Date\"]\n",
    "greatest_date = greatest_date.to_string(index=False)\n",
    "greatest_increase_num = ((\"$ {:,}\".format(greatest_increase_num)))\n",
    "g_increase = [greatest_date, greatest_increase_num]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 407,
   "metadata": {},
   "outputs": [],
   "source": [
    "greatest_decrease_num = file_to_load_df[\"ChangeinProfits\"].min()\n",
    "greatest_date2 = file_to_load_df.loc[file_to_load_df[\"ChangeinProfits\"] == greatest_decrease_num]\n",
    "greatest_date2 = greatest_date2[\"Date\"]\n",
    "greatest_date2 = greatest_date2.to_string(index=False)\n",
    "greatest_decrease_num = ((\"$ {:,}\".format(greatest_decrease_num)))\n",
    "g_decrease = [greatest_date2, greatest_decrease_num]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 408,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>total_months</th>\n",
       "      <td>86</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Total</th>\n",
       "      <td>$ 38,382,578</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Average  Change</th>\n",
       "      <td>$ -2315</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Greatest Increase in Profit</th>\n",
       "      <td>[ Feb-2012, $ 1,926,159.0]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Greatest Decrease in Profit</th>\n",
       "      <td>[ Sep-2013, $ -2,196,167.0]</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                       0\n",
       "total_months                                          86\n",
       "Total                                       $ 38,382,578\n",
       "Average  Change                                  $ -2315\n",
       "Greatest Increase in Profit   [ Feb-2012, $ 1,926,159.0]\n",
       "Greatest Decrease in Profit  [ Sep-2013, $ -2,196,167.0]"
      ]
     },
     "execution_count": 408,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "output_data = pd.DataFrame({\"total_months\":[rows_count],\n",
    "                            \"Total\":[sum_gl],\n",
    "                            \"Average  Change\":[average],\n",
    "                            \"Greatest Increase in Profit\":[g_increase],\n",
    "                            \"Greatest Decrease in Profit\":[g_decrease]})\n",
    "output_data = output_data.T\n",
    "output_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 409,
   "metadata": {},
   "outputs": [],
   "source": [
    "output_data.to_excel(\"jorge_table.xlsx\", index = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
