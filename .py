{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\vknsr\\Anaconda3\\lib\\site-packages\\pandas\\core\\computation\\expressions.py:21: UserWarning: Pandas requires version '2.7.3' or newer of 'numexpr' (version '2.7.1' currently installed).\n",
      "  from pandas.core.computation.check import NUMEXPR_INSTALLED\n"
     ]
    }
   ],
   "source": [
    "#Loading the libraries to read the data set\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
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
       "      <th>Year</th>\n",
       "      <th>Month</th>\n",
       "      <th>MobileWeb_or_Web</th>\n",
       "      <th>Type_of_Customers?</th>\n",
       "      <th>Where_Are_They_comming_from?</th>\n",
       "      <th>Which_Place_in_India?</th>\n",
       "      <th>How_many_Landed_on_our_Page?</th>\n",
       "      <th>How_many_Landed_on_the_our_Page_and_clicked_on_a_button?</th>\n",
       "      <th>How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form?</th>\n",
       "      <th>How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form_and_Completed_and_submited_the_form?</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2019</td>\n",
       "      <td>Jan</td>\n",
       "      <td>Desktop_Website</td>\n",
       "      <td>Existing_Customer</td>\n",
       "      <td>Came_From_Google</td>\n",
       "      <td>Bangalore</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>56892</td>\n",
       "      <td>17178</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2019</td>\n",
       "      <td>Jan</td>\n",
       "      <td>Desktop_Website</td>\n",
       "      <td>Existing_Customer</td>\n",
       "      <td>Came_From_Google</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>41460</td>\n",
       "      <td>11916</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2019</td>\n",
       "      <td>Jan</td>\n",
       "      <td>Desktop_Website</td>\n",
       "      <td>Existing_Customer</td>\n",
       "      <td>Came_From_Google</td>\n",
       "      <td>Dehradun</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>55561</td>\n",
       "      <td>19461</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2019</td>\n",
       "      <td>Jan</td>\n",
       "      <td>Desktop_Website</td>\n",
       "      <td>Existing_Customer</td>\n",
       "      <td>Came_From_Google</td>\n",
       "      <td>Indore</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>320923</td>\n",
       "      <td>110667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2019</td>\n",
       "      <td>Jan</td>\n",
       "      <td>Desktop_Website</td>\n",
       "      <td>Existing_Customer</td>\n",
       "      <td>Came_From_Google</td>\n",
       "      <td>Pune</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>220937</td>\n",
       "      <td>46033</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2155</th>\n",
       "      <td>2021</td>\n",
       "      <td>Dec</td>\n",
       "      <td>Mobile_website</td>\n",
       "      <td>New_Customer</td>\n",
       "      <td>Unidentified_Sources</td>\n",
       "      <td>Bangalore</td>\n",
       "      <td>67299.0</td>\n",
       "      <td>21255.0</td>\n",
       "      <td>6984</td>\n",
       "      <td>1882</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2156</th>\n",
       "      <td>2021</td>\n",
       "      <td>Dec</td>\n",
       "      <td>Mobile_website</td>\n",
       "      <td>New_Customer</td>\n",
       "      <td>Unidentified_Sources</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>430294.0</td>\n",
       "      <td>156510.0</td>\n",
       "      <td>46676</td>\n",
       "      <td>16703</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2157</th>\n",
       "      <td>2021</td>\n",
       "      <td>Dec</td>\n",
       "      <td>Mobile_website</td>\n",
       "      <td>New_Customer</td>\n",
       "      <td>Unidentified_Sources</td>\n",
       "      <td>Dehradun</td>\n",
       "      <td>48713.0</td>\n",
       "      <td>27770.0</td>\n",
       "      <td>7515</td>\n",
       "      <td>2089</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2158</th>\n",
       "      <td>2021</td>\n",
       "      <td>Dec</td>\n",
       "      <td>Mobile_website</td>\n",
       "      <td>New_Customer</td>\n",
       "      <td>Unidentified_Sources</td>\n",
       "      <td>Indore</td>\n",
       "      <td>593021.0</td>\n",
       "      <td>310836.0</td>\n",
       "      <td>161575</td>\n",
       "      <td>78465</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2159</th>\n",
       "      <td>2021</td>\n",
       "      <td>Dec</td>\n",
       "      <td>Mobile_website</td>\n",
       "      <td>New_Customer</td>\n",
       "      <td>Unidentified_Sources</td>\n",
       "      <td>Pune</td>\n",
       "      <td>372897.0</td>\n",
       "      <td>123057.0</td>\n",
       "      <td>48802</td>\n",
       "      <td>19441</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2160 rows ?? 10 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Year Month MobileWeb_or_Web Type_of_Customers?  \\\n",
       "0     2019   Jan  Desktop_Website  Existing_Customer   \n",
       "1     2019   Jan  Desktop_Website  Existing_Customer   \n",
       "2     2019   Jan  Desktop_Website  Existing_Customer   \n",
       "3     2019   Jan  Desktop_Website  Existing_Customer   \n",
       "4     2019   Jan  Desktop_Website  Existing_Customer   \n",
       "...    ...   ...              ...                ...   \n",
       "2155  2021   Dec   Mobile_website       New_Customer   \n",
       "2156  2021   Dec   Mobile_website       New_Customer   \n",
       "2157  2021   Dec   Mobile_website       New_Customer   \n",
       "2158  2021   Dec   Mobile_website       New_Customer   \n",
       "2159  2021   Dec   Mobile_website       New_Customer   \n",
       "\n",
       "     Where_Are_They_comming_from? Which_Place_in_India?  \\\n",
       "0                Came_From_Google             Bangalore   \n",
       "1                Came_From_Google               Chennai   \n",
       "2                Came_From_Google              Dehradun   \n",
       "3                Came_From_Google                Indore   \n",
       "4                Came_From_Google                  Pune   \n",
       "...                           ...                   ...   \n",
       "2155         Unidentified_Sources             Bangalore   \n",
       "2156         Unidentified_Sources               Chennai   \n",
       "2157         Unidentified_Sources              Dehradun   \n",
       "2158         Unidentified_Sources                Indore   \n",
       "2159         Unidentified_Sources                  Pune   \n",
       "\n",
       "      How_many_Landed_on_our_Page?  \\\n",
       "0                              NaN   \n",
       "1                              NaN   \n",
       "2                              NaN   \n",
       "3                              NaN   \n",
       "4                              NaN   \n",
       "...                            ...   \n",
       "2155                       67299.0   \n",
       "2156                      430294.0   \n",
       "2157                       48713.0   \n",
       "2158                      593021.0   \n",
       "2159                      372897.0   \n",
       "\n",
       "      How_many_Landed_on_the_our_Page_and_clicked_on_a_button?  \\\n",
       "0                                                   NaN          \n",
       "1                                                   NaN          \n",
       "2                                                   NaN          \n",
       "3                                                   NaN          \n",
       "4                                                   NaN          \n",
       "...                                                 ...          \n",
       "2155                                            21255.0          \n",
       "2156                                           156510.0          \n",
       "2157                                            27770.0          \n",
       "2158                                           310836.0          \n",
       "2159                                           123057.0          \n",
       "\n",
       "      How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form?  \\\n",
       "0                                                 56892                                       \n",
       "1                                                 41460                                       \n",
       "2                                                 55561                                       \n",
       "3                                                320923                                       \n",
       "4                                                220937                                       \n",
       "...                                                 ...                                       \n",
       "2155                                               6984                                       \n",
       "2156                                              46676                                       \n",
       "2157                                               7515                                       \n",
       "2158                                             161575                                       \n",
       "2159                                              48802                                       \n",
       "\n",
       "      How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form_and_Completed_and_submited_the_form?  \n",
       "0                                                 17178                                                                          \n",
       "1                                                 11916                                                                          \n",
       "2                                                 19461                                                                          \n",
       "3                                                110667                                                                          \n",
       "4                                                 46033                                                                          \n",
       "...                                                 ...                                                                          \n",
       "2155                                               1882                                                                          \n",
       "2156                                              16703                                                                          \n",
       "2157                                               2089                                                                          \n",
       "2158                                              78465                                                                          \n",
       "2159                                              19441                                                                          \n",
       "\n",
       "[2160 rows x 10 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# using pandas read the csv file(dataset)\n",
    "df=pd.read_csv(\"C:/Users/vknsr/Downloads/Fytlyff_DS_Interview.csv\")\n",
    "pd.DataFrame(df) # coverting all values to dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
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
       "      <th>Year</th>\n",
       "      <th>Month</th>\n",
       "      <th>MobileWeb_or_Web</th>\n",
       "      <th>Type_of_Customers?</th>\n",
       "      <th>Where_Are_They_comming_from?</th>\n",
       "      <th>Which_Place_in_India?</th>\n",
       "      <th>How_many_Landed_on_our_Page?</th>\n",
       "      <th>How_many_Landed_on_the_our_Page_and_clicked_on_a_button?</th>\n",
       "      <th>How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form?</th>\n",
       "      <th>How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form_and_Completed_and_submited_the_form?</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2019</td>\n",
       "      <td>Jan</td>\n",
       "      <td>Desktop_Website</td>\n",
       "      <td>Existing_Customer</td>\n",
       "      <td>Came_From_Google</td>\n",
       "      <td>Bangalore</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>56892</td>\n",
       "      <td>17178</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2019</td>\n",
       "      <td>Jan</td>\n",
       "      <td>Desktop_Website</td>\n",
       "      <td>Existing_Customer</td>\n",
       "      <td>Came_From_Google</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>41460</td>\n",
       "      <td>11916</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2019</td>\n",
       "      <td>Jan</td>\n",
       "      <td>Desktop_Website</td>\n",
       "      <td>Existing_Customer</td>\n",
       "      <td>Came_From_Google</td>\n",
       "      <td>Dehradun</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>55561</td>\n",
       "      <td>19461</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2019</td>\n",
       "      <td>Jan</td>\n",
       "      <td>Desktop_Website</td>\n",
       "      <td>Existing_Customer</td>\n",
       "      <td>Came_From_Google</td>\n",
       "      <td>Indore</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>320923</td>\n",
       "      <td>110667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2019</td>\n",
       "      <td>Jan</td>\n",
       "      <td>Desktop_Website</td>\n",
       "      <td>Existing_Customer</td>\n",
       "      <td>Came_From_Google</td>\n",
       "      <td>Pune</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>220937</td>\n",
       "      <td>46033</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Year Month MobileWeb_or_Web Type_of_Customers?  \\\n",
       "0  2019   Jan  Desktop_Website  Existing_Customer   \n",
       "1  2019   Jan  Desktop_Website  Existing_Customer   \n",
       "2  2019   Jan  Desktop_Website  Existing_Customer   \n",
       "3  2019   Jan  Desktop_Website  Existing_Customer   \n",
       "4  2019   Jan  Desktop_Website  Existing_Customer   \n",
       "\n",
       "  Where_Are_They_comming_from? Which_Place_in_India?  \\\n",
       "0             Came_From_Google             Bangalore   \n",
       "1             Came_From_Google               Chennai   \n",
       "2             Came_From_Google              Dehradun   \n",
       "3             Came_From_Google                Indore   \n",
       "4             Came_From_Google                  Pune   \n",
       "\n",
       "   How_many_Landed_on_our_Page?  \\\n",
       "0                           NaN   \n",
       "1                           NaN   \n",
       "2                           NaN   \n",
       "3                           NaN   \n",
       "4                           NaN   \n",
       "\n",
       "   How_many_Landed_on_the_our_Page_and_clicked_on_a_button?  \\\n",
       "0                                                NaN          \n",
       "1                                                NaN          \n",
       "2                                                NaN          \n",
       "3                                                NaN          \n",
       "4                                                NaN          \n",
       "\n",
       "   How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form?  \\\n",
       "0                                              56892                                       \n",
       "1                                              41460                                       \n",
       "2                                              55561                                       \n",
       "3                                             320923                                       \n",
       "4                                             220937                                       \n",
       "\n",
       "   How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form_and_Completed_and_submited_the_form?  \n",
       "0                                              17178                                                                          \n",
       "1                                              11916                                                                          \n",
       "2                                              19461                                                                          \n",
       "3                                             110667                                                                          \n",
       "4                                              46033                                                                          "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#reading the first five data sets of the entire data set, data set contains both catogorical and numeric values and null values\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Year', 'Month', 'MobileWeb_or_Web', 'Type_of_Customers?',\n",
       "       'Where_Are_They_comming_from?', 'Which_Place_in_India?',\n",
       "       'How_many_Landed_on_our_Page?',\n",
       "       'How_many_Landed_on_the_our_Page_and_clicked_on_a_button?',\n",
       "       'How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form?',\n",
       "       'How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form_and_Completed_and_submited_the_form?'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# getting the column names used from the data set\n",
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Year                                                                                                                            0\n",
       "Month                                                                                                                           0\n",
       "MobileWeb_or_Web                                                                                                                0\n",
       "Type_of_Customers?                                                                                                              0\n",
       "Where_Are_They_comming_from?                                                                                                    0\n",
       "Which_Place_in_India?                                                                                                           0\n",
       "How_many_Landed_on_our_Page?                                                                                                 1080\n",
       "How_many_Landed_on_the_our_Page_and_clicked_on_a_button?                                                                     1080\n",
       "How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form?                                           0\n",
       "How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form_and_Completed_and_submited_the_form?       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#getting the total number of null values column wise\n",
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
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
       "      <th>Year</th>\n",
       "      <th>How_many_Landed_on_our_Page?</th>\n",
       "      <th>How_many_Landed_on_the_our_Page_and_clicked_on_a_button?</th>\n",
       "      <th>How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form?</th>\n",
       "      <th>How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form_and_Completed_and_submited_the_form?</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>2160.000000</td>\n",
       "      <td>1.080000e+03</td>\n",
       "      <td>1.080000e+03</td>\n",
       "      <td>2.160000e+03</td>\n",
       "      <td>2.160000e+03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>2020.000000</td>\n",
       "      <td>7.844949e+05</td>\n",
       "      <td>3.584563e+05</td>\n",
       "      <td>1.510725e+05</td>\n",
       "      <td>5.922129e+04</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.816686</td>\n",
       "      <td>1.232518e+06</td>\n",
       "      <td>4.981331e+05</td>\n",
       "      <td>2.353538e+05</td>\n",
       "      <td>8.646564e+04</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>2019.000000</td>\n",
       "      <td>2.456700e+04</td>\n",
       "      <td>8.425000e+03</td>\n",
       "      <td>3.761000e+03</td>\n",
       "      <td>7.660000e+02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2019.000000</td>\n",
       "      <td>1.406165e+05</td>\n",
       "      <td>8.060375e+04</td>\n",
       "      <td>3.360800e+04</td>\n",
       "      <td>1.157725e+04</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>2020.000000</td>\n",
       "      <td>3.818205e+05</td>\n",
       "      <td>1.731775e+05</td>\n",
       "      <td>7.064950e+04</td>\n",
       "      <td>2.700450e+04</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>2021.000000</td>\n",
       "      <td>8.196922e+05</td>\n",
       "      <td>3.948560e+05</td>\n",
       "      <td>1.659590e+05</td>\n",
       "      <td>7.185350e+04</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>2021.000000</td>\n",
       "      <td>1.127413e+07</td>\n",
       "      <td>4.079301e+06</td>\n",
       "      <td>3.022858e+06</td>\n",
       "      <td>1.251258e+06</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Year  How_many_Landed_on_our_Page?  \\\n",
       "count  2160.000000                  1.080000e+03   \n",
       "mean   2020.000000                  7.844949e+05   \n",
       "std       0.816686                  1.232518e+06   \n",
       "min    2019.000000                  2.456700e+04   \n",
       "25%    2019.000000                  1.406165e+05   \n",
       "50%    2020.000000                  3.818205e+05   \n",
       "75%    2021.000000                  8.196922e+05   \n",
       "max    2021.000000                  1.127413e+07   \n",
       "\n",
       "       How_many_Landed_on_the_our_Page_and_clicked_on_a_button?  \\\n",
       "count                                       1.080000e+03          \n",
       "mean                                        3.584563e+05          \n",
       "std                                         4.981331e+05          \n",
       "min                                         8.425000e+03          \n",
       "25%                                         8.060375e+04          \n",
       "50%                                         1.731775e+05          \n",
       "75%                                         3.948560e+05          \n",
       "max                                         4.079301e+06          \n",
       "\n",
       "       How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form?  \\\n",
       "count                                       2.160000e+03                                       \n",
       "mean                                        1.510725e+05                                       \n",
       "std                                         2.353538e+05                                       \n",
       "min                                         3.761000e+03                                       \n",
       "25%                                         3.360800e+04                                       \n",
       "50%                                         7.064950e+04                                       \n",
       "75%                                         1.659590e+05                                       \n",
       "max                                         3.022858e+06                                       \n",
       "\n",
       "       How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form_and_Completed_and_submited_the_form?  \n",
       "count                                       2.160000e+03                                                                          \n",
       "mean                                        5.922129e+04                                                                          \n",
       "std                                         8.646564e+04                                                                          \n",
       "min                                         7.660000e+02                                                                          \n",
       "25%                                         1.157725e+04                                                                          \n",
       "50%                                         2.700450e+04                                                                          \n",
       "75%                                         7.185350e+04                                                                          \n",
       "max                                         1.251258e+06                                                                          "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# knowing more info about the data set before cleaning the data\n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "#data cleaning is performed using replace function\n",
    "def data_cleaning():\n",
    "    df=df.replace(to_replace=np.NaN,value=0)\n",
    "    df['Month'] = pd.to_datetime(df['Month'],format='%b').dt.month\n",
    "    df=df.replace(to_replace=\"Came_From_Google\",value=\"Google\")\n",
    "    df=df.replace(to_replace=\"Landed_on_the_page_Directly\",value=\"Direct_traffic\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#descriptive status\n",
    "def descriptive_status():\n",
    "    df.describe()\n",
    "    df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
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
       "      <th>Year</th>\n",
       "      <th>How_many_Landed_on_our_Page?</th>\n",
       "      <th>How_many_Landed_on_the_our_Page_and_clicked_on_a_button?</th>\n",
       "      <th>How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form?</th>\n",
       "      <th>How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form_and_Completed_and_submited_the_form?</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Which_Place_in_India?</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Bangalore</th>\n",
       "      <td>2021</td>\n",
       "      <td>1645248.0</td>\n",
       "      <td>781237.0</td>\n",
       "      <td>701204</td>\n",
       "      <td>502226</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Chennai</th>\n",
       "      <td>2021</td>\n",
       "      <td>4605196.0</td>\n",
       "      <td>2235411.0</td>\n",
       "      <td>1833439</td>\n",
       "      <td>430733</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Dehradun</th>\n",
       "      <td>2021</td>\n",
       "      <td>2255791.0</td>\n",
       "      <td>1121317.0</td>\n",
       "      <td>994925</td>\n",
       "      <td>873534</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Indore</th>\n",
       "      <td>2021</td>\n",
       "      <td>5706772.0</td>\n",
       "      <td>3406853.0</td>\n",
       "      <td>3022858</td>\n",
       "      <td>1251258</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Pune</th>\n",
       "      <td>2021</td>\n",
       "      <td>11274131.0</td>\n",
       "      <td>4079301.0</td>\n",
       "      <td>1942557</td>\n",
       "      <td>923720</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       Year  How_many_Landed_on_our_Page?  \\\n",
       "Which_Place_in_India?                                       \n",
       "Bangalore              2021                     1645248.0   \n",
       "Chennai                2021                     4605196.0   \n",
       "Dehradun               2021                     2255791.0   \n",
       "Indore                 2021                     5706772.0   \n",
       "Pune                   2021                    11274131.0   \n",
       "\n",
       "                       How_many_Landed_on_the_our_Page_and_clicked_on_a_button?  \\\n",
       "Which_Place_in_India?                                                             \n",
       "Bangalore                                                       781237.0          \n",
       "Chennai                                                        2235411.0          \n",
       "Dehradun                                                       1121317.0          \n",
       "Indore                                                         3406853.0          \n",
       "Pune                                                           4079301.0          \n",
       "\n",
       "                       How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form?  \\\n",
       "Which_Place_in_India?                                                                                          \n",
       "Bangalore                                                         701204                                       \n",
       "Chennai                                                          1833439                                       \n",
       "Dehradun                                                          994925                                       \n",
       "Indore                                                           3022858                                       \n",
       "Pune                                                             1942557                                       \n",
       "\n",
       "                       How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form_and_Completed_and_submited_the_form?  \n",
       "Which_Place_in_India?                                                                                                                             \n",
       "Bangalore                                                         502226                                                                          \n",
       "Chennai                                                           430733                                                                          \n",
       "Dehradun                                                          873534                                                                          \n",
       "Indore                                                           1251258                                                                          \n",
       "Pune                                                              923720                                                                          "
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=df.groupby('Which_Place_in_India?') # to get the city max for each city we use group by method\n",
    "b=a.max(5)\n",
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "# dividing both the columns of b and keep it in c\n",
    "c=b['How_many_Landed_on_our_Page?']/b['How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form_and_Completed_and_submited_the_form?']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Which_Place_in_India?\n",
       "Bangalore     3.275912\n",
       "Chennai      10.691533\n",
       "Dehradun      2.582373\n",
       "Indore        4.560828\n",
       "Pune         12.205139\n",
       "dtype: float64"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c  # from this we can see chennai is highest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "d=df[\"Year\"]=2021 # assigning all values of 2021 to d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import mean_absolute_percentage_error #imported the MAPE from sklearn\n",
    "def pred_future():\n",
    "    b['How_many_Landed_on_the_our_Page_and_clicked_on_a_button_and_started_filling_the_Form_and_Completed_and_submited_the_form?'].predict(\"Year\"==2022)\n",
    "    mean_absolute_percentage_error(df,d)"
   ]
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
