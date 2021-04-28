import sas7bdat_converter 

file_dicts = [
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r102.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r102.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r103.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r103.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r104.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r104.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r105.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r105.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r106.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r106.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r107.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r107.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r108.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r108.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r109.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r109.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r112.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r112.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r113.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r113.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r114.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r114.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r116.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r116.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r118.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r118.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r144.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r144.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r188.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r188.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r202.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r202.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r206.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r206.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r300.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r300.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r301.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r301.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r302.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r302.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r330.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r330.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r331.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r331.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r340.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r340.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r800.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r800.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r801.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/_r801.csv',
  },
  {
    'sas7bdat_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/svrformats64.sas7bdat',
    'export_file': '/Users/nicolewhite/Desktop/CAP6545/Final-Project/data/svrformats64.csv',
  },
]
sas7bdat_converter.batch_to_csv(file_dicts)