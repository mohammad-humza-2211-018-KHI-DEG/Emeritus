# Module 1 - Day 1 - Introduction

## Intro

During this hands-on exercise you will create a basic data lake on AWS using AWS S3,
Glue Crawlers and Athena - services and mechanisms that are available for use on
AWS.

### Prerequisites

Be sure to have a working AWS user account with the required permissions and access
to [AWS Management Console](https://aws.amazon.com/console/).

### Hands-on plan

- [Populating the data lake](#task-1---populating-the-data-lake)
- [Creating a schema table using Glue Crawler](#task-1---creating-a-schema-table-using-glue-crawler)
- [Querying the data using Athena](#task-2---querying-the-data-using-athena)
- [Querying the data using S3 Select](#task-3---querying-the-data-using-s3-select)

## Task 1 - Populating the data lake

Proceed with the following steps:

1. Create a new bucket on S3. Name the bucket with your name and first letter of your
   surname and a suffix: `-module4-day4`.
2. Upload the contents of the `data` directory from the today's exercise's directory in
   the repository to the newly created S3 bucket.

Whether the data was present or not:

1. Create a directory called `athena-query-results` in the existing bucket.

## Task 1 - Creating a schema table using Glue Crawler

1. Go to the Glue service and create a new Crawler. Name the crawler with your name and
   first letter of your surname and a suffix: `_combined_employee_earnings_crawler`.
   When
   creating the crawler, select the `output_data/employee_earnings/` directory as the data
   source.

   Proceed with the creation the same way as in day 2 - we will be reusing the
   database and the IAM role for the crawler.
2. Run the crawler - after it finishes the run successfully, go to the Tables section (
   in the menu on the left) and verify that the table has been created.

## Task 2 - Querying the data using Athena

To query the S3 data using Athena, do the following steps:

1. Go to the Athena service dashboard.
2. If you're not there by default, select `Query editor` from the menu on the left.
3. You will see a message in a blue
   box: `"Before you run your first query, you need to set up a query result location in Amazon S3."`

   To do that, click on `Edit settings` on the right of the message and select the
   `athena_query_results` S3 directory you created earlier.
4. Now we can start querying the data:
    - go into the editor view
    - select `AwsDataCatalog` as the data source
    - select `<your_name><your_surname>_glue_database` as the database
    - refresh the view - you should see a list of tables in the `tables and views`
      section
    - click on the three dots next to the table you've newly created and
      select `Preview table` - this option will create and run an example query on your
      data. Notice how the database and table is referenced in the query.
5. Create a few queries using standard SQL (you can observe how the data is structured
   using the query result from the previous step):
    - All employees from offices 'New York' and 'Scranton' with age > 30.
    - Min, max, average and total earnings for each office and each day - sorted by total earnings, highest to lowest.
    - Difference between worst and best day earnings for every office branch.

## Task 3 - Querying the data using S3 Select

For the next task, run the previous queries using S3 Select and compare the results:

1. Go into S3, into on of the `output_data/employee_earnings/earnings_date` directories and select
   one of the Parquet files present there.
2. Click `Actions` and select `Query with S3 Select`.
3. Select Parquet as input and CSV as output. Run the example query to see the result.
   You can view the results in a raw or a table format.
4. Run the previous queries using S3 Select. What are the advantages/disadvantages of
   using this approach? Are all the queries possible to run?

## Bonus task

Look for more alternatives for building data lakes on AWS.
Get acquainted with a service called [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html).
What advantages does this more advanced approach have over our solution?
