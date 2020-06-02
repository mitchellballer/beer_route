import shapefile
#shapefiles used were download from https://viewer.nationalmap.gov/
#this shapefile contains Polylinem type shapes or shapeType == 23
sf = shapefile.Reader("Trans_RoadSegment")

#find the fields in this dataset
fields = sf.fields
#these are the fields used: 
#[('DeletionFlag', 'C', 1, 0), ['OBJECTID', 'N', 10, 0], ['PERMANENT_', 'C', 40, 0], ['SOURCE_FEA', 'C', 40, 0], ['SOURCE_DAT', 'C', 40, 0], ['SOURCE_D_1', 'C', 100, 0], ['SOURCE_ORI', 'C', 130, 0], ['LOADDATE', 'D', 8, 0], ['INTERSTATE', 'C', 25, 0], ['INTERSTA_1', 'C', 25, 0], ['INTERSTA_2', 'C', 25, 0], ['INTERSTA_3', 'C', 25, 0], ['US_ROUTE', 'C', 25, 0], ['US_ROUTE_A', 'C', 25, 0], ['US_ROUTE_B', 'C', 25, 0], ['US_ROUTE_C', 'C', 25, 0], ['STATE_ROUT', 'C', 25, 0], ['STATE_RO_1', 'C', 25, 0], ['STATE_RO_2', 'C', 25, 0], ['STATE_RO_3', 'C', 25, 0], ['COUNTY_ROU', 'C', 25, 0], ['FEDERAL_LA', 'C', 25, 0], ['STCO_FIPSC', 'C', 5, 0], ['TNMFRC', 'N', 10, 0], ['FULL_STREE', 'C', 100, 0], ['MTFCC_CODE', 'C', 50, 0], ['SHAPE_Leng', 'F', 19, 11]]

#grab a single record from the data
rec = sf.record(3)
#see that records field data
for i in rec:
    print(i)
#Record #3: [4, '{BBED7D86-0D49-4596-8775-A55DDA720E53}', '110439280265', '{F0E1D838-E91D-4F76-8F52-5656F95D5CC3}', '2018 May MAF/TIGER', 'U.S. Department of Commerce, U.S. Census Bureau, Geography Division', datetime.date(2019, 10, 1), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '39141', 4, '', 'S1400', 0.000657497490905]
