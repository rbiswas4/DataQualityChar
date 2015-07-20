
### IO
Reading in light Curves from different sources
#### Input
Do whatever it takes to get light curve into Pandas DataFrame
##### Implementation in different formats:
- SNANA Light curve (ASCII/FITS format): use SNCosmo reader to get the data into `~astropy.Table.Table` format. Convert this to pandas DataFrame by using np.asarray
- ASCII file formats in classification challenge
- CFA file formats ?

#### Serialization of Light Curves
- SNCosmo recognized formats (ASCII, JSON)
- HDF ?


### Attributes
##### Intermediate quantities to be Calculated:
- Do Groupings by filters
- Do groupings based on MJD windows

##### Final Quantities:
- SNRMAX, SNRMAX2, SNRMAX3 (old SNANA type quality filters)
- phase quality: Number of epochs per filter in each m day bin
- Aggregates of such quantities?
- Color type quantities ?
