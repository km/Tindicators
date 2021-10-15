# Tindicators
**Tindicators** is a Python library to calculate the valeus of various technical indicators

## Examples

   
```python
import MovingAverages 
import Volume

#Initializes MovingAverages class with price list
m = MovingAverages.MovingAverages([91,90,89,88,90,882])
#Initializes Volumes class with both a volume and a price list
v = Volume.Volume([25200, 30000, 25600, 32000, 23000, 40000],[10, 10.15, 10.17, 10.13, 10.11, 10.15])
#Prints 20 day SMA assuming there is atleast 20 values in the price list
print(m.SMA(20))
#Prints the 20 day SMA of the 5th day before the latest day
print(m.SMA(20,5))
#Prints the OBV of the latest day
print(v.OBV())
#Prints the OBV of the 5th day before the latest day
print(v.OBV(5))
 
```
## Notes:

- Make sure you have enough prices or volume values in the list for the time period you use.
- More indicators soon!
