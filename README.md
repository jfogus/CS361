#CS361 Life Generator - Sprint 3
*Proof of Concept*

## How to Run:
1. Place a data file named `amazon_co-ecommerce_sample.csv`
   in the same directory as `life_generator.py`.
   
   a. If wanting to import filters. Place a csv file named
      `input.csv` also in the same directory as
      `life_generator.py`.

2. At a command prompt, navigate to the directory in which
   `life_generator.py` exists.

3.
    a. Type `python3 life_generator.py` to run the application
       without the optional file argument. This will start the
       GUI.
    
    b. Type `python3 life_generator.py input.csv` to run the
       application and produce the output without user input.
   
4. Output will be saved in the form of a CSV file at 
   `output.csv`.
   
### Note:
* `input.csv` must have headers and be in the form `input_item_type, input_item_category, input_number_to_generate`.
* `amazon_co-ecommerce_sample.csv` must be pulled from kaggle at https://www.kaggle.com/PromptCloudHQ/toy-products-on-amazon.
* `output.csv` will be in the form `input_item_type, input_item_category, input_number_to_generate, output_item_name, output_item_rating, output_item_num_reviews`.
