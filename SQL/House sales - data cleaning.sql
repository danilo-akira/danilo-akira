
-- This dataset contains information about house sales in USA. It is a raw dataset and needs to be cleaned.

-- Exploring the dataset

SELECT * FROM HouseSales
SELECT COUNT(*) FROM HouseSales
SELECT COUNT(distinct ID) FROM HouseSales

	-- The dataset contains 1239 observations. There are 7 columns: ID, Address (street, region, city and state), Sale Date (mm/dd/yyyy), Price, Bedrooms and Status
	-- The count distinct query shows that IDs are not unique or there are some duplicated data
	-- We can see at a first look that some of the data is missing and some of it seems to be mispelled or is not following a pattern in terms of format

-- Checking for Null values

SELECT * 
FROM HouseSales 
WHERE ID is null or Type is null or Address is null or [Sale Date] is null or Price is null or Bedrooms is null or Status is null

	-- The query shows that there are not null values in the dataset, but we see that some of the data are blank. Let's check if they are ''.

SELECT * 
FROM HouseSales 
WHERE ID = '' or Type = '' or Address = '' or [Sale Date] = '' or Price = '' or Bedrooms = '' or Status = ''

	-- The query shows that there are 13 rows that contains at least 1 blank data. There is no ID, Bedrooms or Status in blank, but Type, Address, Sale Date and Price contain blank data.
	-- Since they represent a small percentage of the sample, we'll delete them from the dataset. 

-- Deleting every row that contains blank data

DELETE FROM HouseSales
WHERE ID = '' or Type = '' or Address = '' or [Sale Date] = '' or Price = '' or Bedrooms = '' or Status = ''

	-- Checking update

SELECT * 
FROM HouseSales 
WHERE ID = '' or Type = '' or Address = '' or [Sale Date] = '' or Price = '' or Bedrooms = '' or Status = ''

	-- No rows found

-- Checking for duplicate rows

SELECT ID, COUNT(ID)
FROM HouseSales
group by ID
having COUNT(ID) > 1

	-- There are 4 duplicate IDs. 

SELECT * FROM HouseSales
WHERE ID = 74 or ID = 75 or ID = 79 or ID = 80
ORDER BY ID

	-- All data in these rows are duplicate. Let's remove them

WITH query (ID, row_n) as (
SELECT ID, ROW_NUMBER() over(
PARTITION BY ID
ORDER BY ID) as row_n
FROM HouseSales)

DELETE FROM query
WHERE row_n > 1

SELECT ID, COUNT(ID)
FROM HouseSales
group by ID
having COUNT(ID) > 1

	-- Duplicate rows deleted

-- Next, I'll explore each column searching for mistakes

SELECT distinct Type FROM HouseSales

	-- There is 'Detached' and 'Detached House', but both mean the same. Also, there is 'Semi-detached' and 'Semi detached'. Let's correct the mistakes

UPDATE HouseSales
SET Type = 'Detached' WHERE Type = 'Detached House'

UPDATE HouseSales
SET Type = 'Semi-detached' WHERE Type = 'Semi detached'

-- Address informs the street, region, city and state. It would be better if location levels were separated, so that we can analyze grouping by each of them

	-- Creating support column
ALTER TABLE HouseSales
ADD Address2 nvarchar(255)
UPDATE HouseSales
SET Address2 = Address

	-- Creating new columns
ALTER TABLE HouseSales
ADD Street nvarchar(255)

ALTER TABLE HouseSales
ADD Region nvarchar(255)

ALTER TABLE HouseSales
ADD City nvarchar(255)

ALTER TABLE HouseSales
ADD State nvarchar(255)

	-- Adding data
UPDATE HouseSales
SET Street = SUBSTRING(Address2, 1, CHARINDEX(';', Address2) - 1)

UPDATE HouseSales
SET Address2 = STUFF(Address2, 1, CHARINDEX(';', Address2), '')

UPDATE HouseSales
SET Region = SUBSTRING(Address2, 1, CHARINDEX(';', Address2) - 1)

UPDATE HouseSales
SET Address2 = STUFF(Address2, 1, CHARINDEX(';', Address2), '')

UPDATE HouseSales    
SET	City = SUBSTRING(Address2, 1, CHARINDEX(';', Address2) - 1)

UPDATE HouseSales
SET Address2 = STUFF(Address2, 1, CHARINDEX(';', Address2), '')

UPDATE HouseSales
SET State = Address2

	-- Deleting support column
ALTER TABLE HouseSales
drop column Address2

-- Checking Sale Date column

SELECT distinct SUBSTRING([Sale Date], 1, 2) FROM HouseSales
SELECT distinct SUBSTRING([Sale Date], 3, 3) FROM HouseSales
SELECT distinct SUBSTRING([Sale Date], 6, 5) FROM HouseSales
	
	-- All dates are on mm/dd/yyy format, but some of them have '-' instead of '/'

UPDATE HouseSales
SET [Sale Date]= REPLACE([Sale Date], '-', '/')

-- Checking Price column

SELECT distinct Price FROM HouseSales
	
	-- Some of the prices have a '$' sign. Let's remove it

UPDATE HouseSales
SET Price = REPLACE(Price, '$', '')

-- Checking Bedrooms column

SELECT distinct Bedrooms FROM HouseSales

	-- Bedrooms column is all fine

-- Checking Status column

SELECT distinct Bedrooms FROM HouseSales

	-- Status column has 3 different values: New, Owned or '?'. Since '?' means an unknown information, let's see how many observations they represent

SELECT count(*) 
FROM HouseSales 
WHERE Status = '?'
	
	-- There are only 3 rows with '?'. Removing them will not impact our sample to future analysis

DELETE FROM HouseSales
WHERE Status = '?'

-- Finally, we'll be changing the data type of the columns that are not string

ALTER TABLE HouseSales ALTER COLUMN ID int
ALTER TABLE HouseSales ALTER COLUMN Price int
ALTER TABLE HouseSales ALTER COLUMN Bedrooms int
UPDATE HouseSales 
SET [Sale Date] = CONVERT(DATETIME,[Sale Date],101)
ALTER TABLE HouseSales ALTER COLUMN [Sale Date] date

-- Now the cleaning is complete and the dataset is ready for analysis