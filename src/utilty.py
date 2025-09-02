import numpy as np 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

"""
Note: After modifying this file, it is recommended to delete the __pycache__ directory within the src folder and restart your development environment (e.g., VS Code). This ensures that Python recompiles the updated source code and prevents potential issues caused by stale bytecode.
"""





def generate_csv( df ,lst,name):
    
    """Saves a Pandas DataFrame or Series to a CSV file with new column names. 📄

    This function takes a Pandas DataFrame or Series, renames its columns
    using the provided list, and then exports the result to a CSV file.
    If a Series is provided, it is first converted into a two-column
    DataFrame before being processed.

    Args:
        df (pd.DataFrame or pd.Series): The input data to be saved.

        lst (list): A list of strings to be used as the new column names.

        name (str): The desired name for the output CSV file, without the
            .csv extension.

    Returns:
        None: This function does not return any value; it saves a file to disk.
        
    Raises:
        ValueError: If the length of `lst` does not match the number of
            columns in the DataFrame.
    """

    # This Funtion is used to generate csv reports from the notebook

    if isinstance(df, pd.Series):
        df_csv = df.reset_index()
    else:
        df_csv = df
    

    
    # lst = []
    # for i in range(0,len(df_csv.columns)):
    #     col = input(f"Enter the name of {i+1} column : ")
    #     lst+=col

    
    df_csv.columns = lst 

    # name = input("Enter the name of your csv : ")

    df_csv.to_csv(f'{name}.csv',index = False , encoding = 'utf-8')




def annotate_plot(ax , orient ='v',values = int):

    """Adds value labels to the bars of a Matplotlib axes object. ✍️

    This function iterates over the patches (bars) in a plot and places a
    text annotation on each bar, representing its value. It supports both
    vertical and horizontal bar plots and allows for formatting labels as
    integers or floats.

    Args:
        ax (matplotlib.axes.Axes): The specific chart or subplot you want to label. 
            Think of this as the "canvas" 🖼️ where your bar plot is drawn.

        orient (str, optional): The orientation of the bar plot.
            Accepts 'v' for vertical or 'h' for horizontal.
            Defaults to 'v'.

        values (type, optional): The data type for formatting the labels.
            Accepts int or float. Defaults to int.

    Returns:
        None: The function modifies the input axes object in place.

    Example:
        >>> import seaborn as sns
        >>> import matplotlib.pyplot as plt
        >>>
        >>> # Sample data
        >>> tips = sns.load_dataset("tips")
        >>>
        >>> # Create a vertical bar plot
        >>> fig, ax = plt.subplots()
        >>> sns.barplot(x="day", y="total_bill", data=tips, ax=ax, estimator=sum)
        >>> ax.set_title("Total Bill by Day (Vertical)")
        >>>
        >>> # Annotate the plot
        >>> annotate_plot(ax, orient='v', values=int)
        >>> plt.show()
    """


    # Loop through each bar in the plot
    for bar in ax.patches:  # ax.patches has a list of shape and dimensions of each bar 

        if orient == 'v': # for vertical orientation
        
            y_value = bar.get_height()
            # bar.get_height() give the height of bar/patch
            
            
            x_value = bar.get_x() + bar.get_width() / 2
            # 1.bar.get_x() gives the coordinates of left-most edge of bar on Canva
            # 2.bar.get_width() gives the width of each bar 
            
            if values == float:
                label = f"{y_value}"
            elif values == int :
                label = f"{int(y_value)}"

            
            # ax.text() Place the text on the plot
            ax.text(x_value, y_value, label, ha='center', va='bottom', fontsize=12)
            # 1. x_values and y_values are (x,y)coordinates on canva where text is to be placed
            # 2. ha stands for Horizontal Alignment 
            # 3. va stands for Vertical Alignment 
        
        elif orient == 'h': # for horizontal orientation
            x_value = bar.get_width()
            # bar.get_height() give the width of bar/patch
            
            
            y_value = bar.get_y() + bar.get_height() / 2
            # 1.bar.get_y() gives the coordinates of top-most edge of bar on Canva
            # 2.bar.get_height() gives the height of each bar 
            
            
            if values == float:
                label = f"{x_value}"
            elif values == int :
                label = f"{int(x_value)}"
            
            
            # ax.text() Place the text on the plot
            ax.text(x_value, y_value, label, ha='left', va='center', fontsize=12)
            # 1. x_values and y_values are (x,y)coordinates on canva where text is to be placed
            # 2. ha stands for Horizontal Alignment 
            # 3. va stands for Vertical Alignment

