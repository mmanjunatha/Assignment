## Run unit test cases:

Follow below steps to run test cases:
> Note: Assuming already python and pip available in the server
- Install pandas package using pip command:
   ```
   pip install pandas
   ```
- clone or get the task.py(from root folder), test.py and orders.csv into your server and place all the files in same directory.
- run below command to run test cases.
   ```
   python -m unittest test
   ```
- Expected output:
   ```
    d:\task\Assignment>python -m unittest test
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.031s
    
    OK
   ```
   
> Note: If you don't have python in local and want to execute with Docker, Kindly follow below steps

- clone or get the task.py(from root folder), test.py, orders.csv and Dockerfile into your server and place all the files in same directory.
- Kindly place the orders.cvs file in the server with proper deatils.
- run below command generate docker image.
```
dcoker build -t testrevenueimage -f Dockerfile .
```
Above step will create image.
- Run below command to get the out put.
```
docker run --rm --name testrevenuetask testrevenueimage
```
This will print the expected output

