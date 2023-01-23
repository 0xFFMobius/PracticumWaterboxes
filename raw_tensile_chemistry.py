#%% ############################################
# Module to retrieve tensile and chemistry response data.
# Target database is oracle, and requires different driver
# Experimenting with the oracle module oracledb as rewrite of 
# cx_Oracle. oracledb allows for direct querying, where as
# cx_Oracle needed a bulky set of supplemental drivers
# sqlalchemy 2.0.0rc3 was used, as version 1.46 did not support
# oracledb.

# Import standard modules
import os
import pandas as pd

# Import additional modules for communicating with the db
from sqlalchemy import create_engine, text

# Import self made modules to hide the connection string, and 
# clean the data from the data base.
from sqlconnection import connection_tensile
from sizeconversion import frac_to_dec, frac_to_dec_str
from predictivetensiles import predictive_tensile_HC9
from idealdiameter import di, di_seg

# Set default ranges for 
START='2012-01-01'
END='2050-01-01'


# SQL strategy:
# SQL statements are modular gathering data from multiple tables
# depending on the product being tested.
# The formats of the tables are similar, but not directly compatible
# so multiple dummy columns are used to have the tables align using
# a final union query.
# Chemistry can also be joined to the tensile data because of 
# the modular layout.

# The use of `begin-sql` and `end-sql` is for a syntax highlighter

# SQL statement to gather tensile data from the rod data table
sql_rod = """
    --begin-sql
    SELECT
        HCROD_S as "Schedule_ID"
        ,test.HEAT as "Schedule_Heat"
        ,GRADE as "Schedule_Grade"
        ,CARD_NO as "Schedule_GradeCard"
        ,FIC_WIP as "Schedule_SPIN"
        --,DESCR as "Schedule_Description"
        ,SPEC.ROD_SIZE as "Schedule_Size"
        ,COIL_ID1 as "Coil_1"
        ,COIL_ID2 as "Coil_2"
        ,COIL_ID3 as "Coil_3"
        ,COIL_ID4 as "Coil_4"
        ,COIL_ID5 as "Coil_5"
        ,COIL_ID6 as "Coil_6"
        ,COIL_ID7 as "Coil_7"
        ,COIL_ID8 as "Coil_8"
        ,COIL_ID9 as "Coil_9"
        ,COIL_ID10 as "Coil_10"
        ,ADIAM1 as "DimIni_1"
        ,ADIAM2 as "DimIni_2"
        ,ADIAM3 as "DimIni_3"
        ,ADIAM4 as "DimIni_4"
        ,ADIAM5 as "DimIni_5"
        ,ADIAM6 as "DimIni_6"
        ,ADIAM7 as "DimIni_7"
        ,ADIAM8 as "DimIni_8"
        ,ADIAM9 as "DimIni_9"
        ,ADIAM10 as "DimIni_10"
        ,AD_N as "DimIni_N"
        ,AD_MIN as "DimIni_MIN"
        ,AD_MAX as "DimIni_MAX"
        ,AD_AVG as "DimIni_AVG"
        ,AD_STD as "DimIni_STD"
        ,RDIAM1 as "DimRed_1"
        ,RDIAM2 as "DimRed_2"
        ,RDIAM3 as "DimRed_3"
        ,RDIAM4 as "DimRed_4"
        ,RDIAM5 as "DimRed_5"
        ,RDIAM6 as "DimRed_6"
        ,RDIAM7 as "DimRed_7"
        ,RDIAM8 as "DimRed_8"
        ,RDIAM9 as "DimRed_9"
        ,RDIAM10 as "DimRed_10"
        ,RD_N as "DimRed_N"
        ,RD_MIN as "DimRed_MIN"
        ,RD_MAX as "DimRed_MAX"
        ,RD_AVG as "DimRed_AVG"
        ,RD_STD as "DimRed_STD"
        ,YLD1/1000 as "YS_1"
        ,YLD2/1000 as "YS_2"
        ,YLD3/1000 as "YS_3"
        ,YLD4/1000 as "YS_4"
        ,YLD5/1000 as "YS_5"
        ,YLD6/1000 as "YS_6"
        ,YLD7/1000 as "YS_7"
        ,YLD8/1000 as "YS_8"
        ,YLD9/1000 as "YS_9"
        ,YLD10/1000 as "YS_10"
        ,YLD_N as "YS_N"
        ,YLD_MIN/1000 as "YS_MIN"
        ,YLD_MAX/1000 as "YS_MAX"
        ,YLD_AVG/1000 as "YS_AVG"
        ,YLD_STD/1000 as "YS_STD"
        ,ULT1/1000 as "UT_1"
        ,ULT2/1000 as "UT_2"
        ,ULT3/1000 as "UT_3"
        ,ULT4/1000 as "UT_4"
        ,ULT5/1000 as "UT_5"
        ,ULT6/1000 as "UT_6"
        ,ULT7/1000 as "UT_7"
        ,ULT8/1000 as "UT_8"
        ,ULT9/1000 as "UT_9"
        ,ULT10/1000 as "UT_10"
        ,ULT_N as "UT_N"
        ,ULT_MIN/1000 as "UT_MIN"
        ,ULT_MAX/1000 as "UT_MAX"
        ,ULT_AVG/1000 as "UT_AVG"
        ,ULT_STD/1000 as "UT_STD"
        ,ELONG1 as "EL_1"
        ,ELONG2 as "EL_2"
        ,ELONG3 as "EL_3"
        ,ELONG4 as "EL_4"
        ,ELONG5 as "EL_5"
        ,ELONG6 as "EL_6"
        ,ELONG7 as "EL_7"
        ,ELONG8 as "EL_8"
        ,ELONG9 as "EL_9"
        ,ELONG10 as "EL_10"
        ,EL_N
        ,EL_MIN
        ,EL_MAX
        ,EL_AVG
        ,EL_STD
        ,RED1 as "RA_1"
        ,RED2 as "RA_2"
        ,RED3 as "RA_3"
        ,RED4 as "RA_4"
        ,RED5 as "RA_5"
        ,RED6 as "RA_6"
        ,RED7 as "RA_7"
        ,RED8 as "RA_8"
        ,RED9 as "RA_9"
        ,RED10 as "RA_10"
        ,RED_N as RA_N
        ,RED_MIN as RA_MIN
        ,RED_MAX as RA_MAX
        ,RED_AVG as RA_AVG
        ,RED_STD as RA_STD
        ,OOR1 as "OV_1"
        ,OOR2 as "OV_2"
        ,OOR3 as "OV_3"
        ,OOR4 as "OV_4"
        ,OOR5 as "OV_5"
        ,OOR6 as "OV_6"
        ,OOR7 as "OV_7"
        ,OOR8 as "OV_8"
        ,OOR9 as "OV_9"
        ,OOR10 as "OV_10"
        ,OOR_N as OV_N
        ,OOR_MIN as OV_MIN
        ,OOR_MAX as OV_MAX
        ,OOR_AVG as OV_AVG
        ,OOR_STD as OV_STD
        , NULL as "WT_1"
        , NULL as "WT_2"
        , NULL as "WT_3"
        , NULL as "WT_4"
        , NULL as "WT_5"
        , NULL as "WT_6"
        , NULL as "WT_7"
        , NULL as "WT_8"
        , NULL as "WT_9"
        , NULL as "WT_10"
        , NULL as "WT_N"
        , NULL as "WT_MIN"
        , NULL as "WT_MAX"
        , NULL as "WT_AVG" 
        , NULL as "WT_STD"
        ,LH_TEMP as "Stelmor_LHTemp"
        ,STELMOOR as "Stelmor_DeckCode"
        {chem}
        --,COMPFLAG as "MTR_Compflag"
        --,TEST_BY as "MTR_TestedBy"
        ,TESTDATE as "MTR_Date"
        ,STATUS as "MTR_Status"
        --,NOTES as "MTR_Notes"
        --,VER_BY as "MTR_VerifiedBy"
        --,PR_TENS as "UT_Predict"
        --,PR_DELTA
        --,TURN as "Schedule_Crew"
        --,TAPDATE as "Schedule_TapDate"
        ,CREATION_DATE as "MTR_CreationDate"
        --,CREATED_BY as MTR_Creator
        ,LAST_UPDATE_DATE as "MTR_Updated"
        --,LAST_UPDATED_BY as MTR_UpdateOwner
        ,CUSTNO as "Schedule_CustomerNo"
    FROM qa.hcrod test 
    --end-sql
"""
# SQL statement to gather tensile data from the rebar data table
sql_bar = """
    --begin-sql
    SELECT 
        MBAR4_S as "Schedule_ID"
        , test.HEAT as "Schedule_Heat"
        , CARD_NO as "Schedule_GradeCard"
        ,FIC_WIP as "Schedule_SPIN"
        , CARD_NO as "Schedule_Grade"
        ,SPEC.ROD_SIZE as "Schedule_Size"
        , NULL as "Coil_1"
        , NULL as "Coil_2"
        , NULL as "Coil_3"
        , NULL as "Coil_4"
        , NULL as "Coil_5"
        , NULL as "Coil_6"
        , NULL as "Coil_7"
        , NULL as "Coil_8"
        , NULL as "Coil_9"
        , NULL as "Coil_10"
        , ADIAM1 as "DimIni_1"
        , ADIAM2 as "DimIni_2"
        , NULL as "DimIni_3"
        , NULL as "DimIni_4"
        , NULL as "DimIni_5"
        , NULL as "DimIni_6"
        , NULL as "DimIni_7"
        , NULL as "DimIni_8"
        , NULL as "DimIni_9"
        , NULL as "DimIni_10"
        , NULL as "DimIni_N"
        , LEAST(ADIAM1, ADIAM2) as "DimIni_MIN"
        , GREATEST(ADIAM1, ADIAM2) as "DimIni_MAX"
        , (ADIAM1 + ADIAM2)/2 as "DimIni_AVG"
        , NULL as "DimIni_STD"
        , RDIAM1 as "DimRed_1"
        , RDIAM2 as "DimRed_2"
        , NULL as "DimRed_3"
        , NULL as "DimRed_4"
        , NULL as "DimRed_5"
        , NULL as "DimRed_6"
        , NULL as "DimRed_7"
        , NULL as "DimRed_8"
        , NULL as "DimRed_9"
        , NULL as "DimRed_10"
        , NULL as "DimRed_N"
        , LEAST(RDIAM1, RDIAM2) as "DimRed_MIN"
        , GREATEST(RDIAM1, RDIAM2) as "DimRed_MAX"
        , (RDIAM1 + RDIAM2)/2 as "DimRed_AVG"
        , NULL as "DimRed_STD"
        , YLD_PSI/1000 as "YS_1"
        , YLD2_PSI/1000 as "YS_2"
        , NULL as "YS_3"
        , NULL as "YS_4"
        , NULL as "YS_5"
        , NULL as "YS_6"
        , NULL as "YS_7"
        , NULL as "YS_8"
        , NULL as "YS_9"
        , NULL as "YS_10"
        , NULL as "YS_N"
        , LEAST(YLD_PSI/1000, YLD2_PSI/1000) as "YS_MIN"
        , GREATEST(YLD_PSI/1000, YLD2_PSI/1000) as "YS_MAX"
        , (YLD_PSI + YLD2_PSI) / 2000 as "YS_AVG"
        , NULL as "YS_STD"
        , ULT_PSI/1000 as "UT_1"
        , ULT2_PSI/1000 as "UT_2"
        , NULL as "UT_3"
        , NULL as "UT_4"
        , NULL as "UT_5"
        , NULL as "UT_6"
        , NULL as "UT_7"
        , NULL as "UT_8"
        , NULL as "UT_9"
        , NULL as "UT_10"
        , NULL as "UT_N"
        , LEAST(ULT_PSI/1000, ULT2_PSI/1000) as "UT_MIN"
        , GREATEST(ULT_PSI/1000, ULT2_PSI/1000) as "UT_MAX"
        , (ULT_PSI + ULT2_PSI) / 2000 as "UT_AVG"
        , NULL as "UT_STD"
        , ELONG as "EL_1"
        , ELONG2 as "EL_2"
        , NULL as "EL_3"
        , NULL as "EL_4"
        , NULL as "EL_5"
        , NULL as "EL_6"
        , NULL as "EL_7"
        , NULL as "EL_8"
        , NULL as "EL_9"
        , NULL as "EL_10"
        , NULL as EL_N
        , LEAST(ELONG, ELONG2) as EL_MIN
        , GREATEST(ELONG, ELONG2) as EL_MAX
        , (ELONG + ELONG2)/2 as EL_AVG
        , NULL as EL_STD
        , NULL as "RA_1"
        , NULL as "RA_2"
        , NULL as "RA_3"
        , NULL as "RA_4"
        , NULL as "RA_5"
        , NULL as "RA_6"
        , NULL as "RA_7"
        , NULL as "RA_8"
        , NULL as "RA_9"
        , NULL as "RA_10"
        , NULL as RA_N
        , NULL as RA_MIN
        , NULL as RA_MAX
        , NULL as RA_AVG
        , NULL as RA_STD
        , NULL as "OV_1"
        , NULL as "OV_2"
        , NULL as "OV_3"
        , NULL as "OV_4"
        , NULL as "OV_5"
        , NULL as "OV_6"
        , NULL as "OV_7"
        , NULL as "OV_8"
        , NULL as "OV_9"
        , NULL as "OV_10"
        , NULL as OV_N
        , NULL as OV_MIN
        , NULL as OV_MAX
        , NULL as OV_AVG
        , NULL as OV_STD
        , GRAMS1 * 0.0022046226 / 2 as "WT_1"
        , GRAMS2 * 0.0022046226 / 2 as "WT_2"
        , NULL as "WT_3"
        , NULL as "WT_4"
        , NULL as "WT_5"
        , NULL as "WT_6"
        , NULL as "WT_7"
        , NULL as "WT_8"
        , NULL as "WT_9"
        , NULL as "WT_10"
        , NULL as "WT_N"
        , LEAST(GRAMS1, GRAMS2) * 0.0022046226 / 2 as "WT_MIN"
        , GREATEST(GRAMS1, GRAMS2) * 0.0022046226 / 2 as "WT_MAX"
        , (GRAMS1 + GRAMS2)/2 * 0.0022046226 / 2 as "WT_AVG" 
        , NULL as "WT_STD"
        , NULL as "Stelmor_LHTemp"
        , NULL as "Stelmor_DeckCode"
        {chem}
        , TESTDATE as "MTR_Date"
        , STATUS as "MTR_Status"
        , CREATION_DATE as "MTR_CreationDate"
        , LAST_UPDATE_DATE as "MTR_Updated"
        , CUSTNO as "Schedule_CustomerNo"
    FROM QA.MBAR4 test
    --end-sql
"""

# SQL statement to gather tensile data from the chemistry table
# Chemistry is stored in multiple locations, depending on if it 
# was melted internally, or purchased externally. 
# The results of the second table is added to the first only if 
# it isn't found in the first table.
# Used to build a subquery
chem_avg = """
    --begin-sql chem_avg
    --HEATS FROM STL_ANL60_CHEM_A
    SELECT
        HEAT
        ,MAX(CHEM_SAMPLE_SEQ) as "Chem_SampleSeq"
        ,AVG(CHEM_CARBON) as "Chem_C"
        ,AVG(CHEM_MANGANESE) as "Chem_Mn"
        ,AVG(CHEM_PHOSPHORUS) as "Chem_P"
        ,AVG(CHEM_SULFUR) as "Chem_S"
        ,AVG(CHEM_SILICON) as "Chem_Si"
        ,AVG(CHEM_COPPER) as "Chem_Cu"
        ,AVG(CHEM_NICKEL) as "Chem_Ni"
        ,AVG(CHEM_CHROME) as "Chem_Cr"
        ,AVG(CHEM_MOLYBDENUM) as "Chem_Mo"
        ,AVG(CHEM_ALUM_TOT) as "Chem_Al"
        ,AVG(CHEM_VANADIUM) as "Chem_V"
        ,AVG(CHEM_BORON) as "Chem_B"
        ,AVG(CHEM_COLUMBIUM) as "Chem_Nb"
        ,AVG(CHEM_TIN) as "Chem_Sn"
        ,AVG(CHEM_ARSENIC) as "Chem_As"
        ,AVG(CHEM_ZINC) as "Chem_Zn"
        ,AVG(CHEM_TITANIUM) as "Chem_Ti"
        ,AVG(CHEM_COBALT) as "Chem_Co"
        ,AVG(CHEM_TUNGSTEN) as "Chem_W"
        ,AVG(CHEM_CALCIUM) as "Chem_Ca"
        ,AVG(CHEM_CERIUM) as "Chem_Ce"
        ,AVG(CHEM_ZIRCONIUM) as "Chem_Zr"
        ,AVG(CHEM_ANTIMONY) as "Chem_Sb"
        ,AVG(CHEM_NITROGEN) as "Chem_N"
        ,AVG(CHEM_OXYGEN) as "Chem_O"
        ,AVG(CHEM_LEAD) as "Chem_Pb"
        ,AVG(CHEM_HYDROGEN) as "Chem_H"
    FROM STL.STL_ANL60_CHEM_A
    WHERE CHEM_SAMPLE_TYPE IN('T1','T2','T3')
    GROUP BY HEAT
    --Heats from LCHM
    UNION SELECT
        HEAT
        ,'0' as "Chem_SampleSeq"
        ,CARBON as "Chem_C"
        ,MANGANESE as "Chem_Mn"
        ,PHOSPHORUS as "Chem_P"
        ,SULFUR as "Chem_S"
        ,SILICON as "Chem_Si"
        ,COPPER as "Chem_Cu"
        ,NICKEL as "Chem_Ni"
        ,CHROME as "Chem_Cr"
        ,MOLYBDENUM as "Chem_Mo"
        ,ALUMINUM_TOTAL as "Chem_Al"
        ,VANADIUM as "Chem_V"
        ,BORON as "Chem_B"
        ,COLUMBIUM as "Chem_Nb"
        ,TIN as "Chem_Sn"
        ,ARSENIC as "Chem_As"
        ,NULL as "Chem_Zn"
        ,TITANIUM as "Chem_Ti"
        ,COBALT as "Chem_Co"
        ,WOLFRAM as "Chem_W"
        ,CALCIUM as "Chem_Ca"
        ,CERIUM as "Chem_Ce"
        ,ZIRCONIUM as "Chem_Zr"
        ,ANTIMONY as "Chem_Sb"
        ,NITROGEN as "Chem_N"
        ,OXYGEN as "Chem_O"
        ,LEAD as "Chem_Pb"
        ,HYDROGEN as "Chem_H"
    FROM QA.LCHM
    WHERE HEAT NOT IN (SELECT HEAT FROM STL.STL_ANL60_CHEM_A)
    --end-sql
"""

# Select statement when chemistry desired to be included.
select_chem = """
    --begin-sql select_chem
        ,"Chem_C"
        ,"Chem_Mn"
        ,"Chem_P"
        ,"Chem_S"
        ,"Chem_Si"
        ,"Chem_Cu"
        ,"Chem_Ni"
        ,"Chem_Cr"
        ,"Chem_Mo"
        ,"Chem_Al"
        ,"Chem_V"
        ,"Chem_B"
        ,"Chem_Nb"
        ,"Chem_Sn"
        ,"Chem_As"
        ,"Chem_Zn"
        ,"Chem_Ti"
        ,"Chem_Co"
        ,"Chem_W"
        ,"Chem_Ca"
        ,"Chem_Ce"
        ,"Chem_Zr"
        ,"Chem_Sb"
        ,"Chem_N"
        ,"Chem_O"
        ,"Chem_Pb"
        ,"Chem_H"
    --end-sql
    """

# formatted python code to join chemistry subquery, when requested
join_chem = '''
    --begin-sql
    INNER JOIN (
        {}
        ) CHEM ON test.HEAT = CHEM.HEAT
    --end-sql
    '''.format(chem_avg)

# formatted python code to join tensile data subquery, when requested
join_rodsize = '''
    --begin-sql
    LEFT JOIN (
        SELECT 
            FWIP,
            PRODUCT_SIZE as "ROD_SIZE"
        FROM qa.fwip2
    ) SPEC ON test.FIC_WIP = SPEC.FWIP
    --end-sql
'''

# A filtering where statement limiting date range
where = """
    --begin-sql
    WHERE (
        TESTDATE BETWEEN TO_DATE('{start}', 'yyyy-mm-dd') 
            AND TO_DATE('{end}', 'yyyy-mm-dd')
        )
    --end-sql
"""

# Formatting the table output
def stack_tensile(df):
    ''' Return tensile data in long format, not wide, no aggregates
    Each test will return on its own line, first normal form. By default 
    tensile data has one column per test, and additional columns for aggregates.
    Data table is in a reporting format, not well formatted normal form.
    '''
    # Test characteristics, with multiple responses. Up to 10 test columns per.
    tests = ['Coil', 'DimIni', 'DimRed', 'YS', 'UT', 'EL', 'RA', 'OV', 'WT']
    # Test results for each section will be processed individually, and 
    # combined
    test_results = []
    value_vars = [str(n) for n in range(1,11)] # tests are number 1-10
    # Some error checking, Coil numbers are manually entered into a text field.
    # This is not validated upon operator entry. 
    try:
        df['Coil'] = df['Coil'].astype(float)
    except ValueError:
        # Check and report each line for the ones which need correction
        print('Following heats have invalid Coil values:')
        temp = df['Coil'].set_index(df[('Schedule', 'Heat')])
        def verify(row):
            try:
                row.astype(float)
            except ValueError:
                print(row)
        temp.apply(verify, axis=1)
    # Now rearrange each sub test into first normal form using melt.
    for test in tests:
        result = (
            df
            [test]
            [value_vars]
            .melt(
                ignore_index=False, 
                value_name=test,
                var_name='TestNum'
                )
            .set_index('TestNum', append=True)
        )
        test_results.append(result)
    # Concatenate the rearranged data together into a single table
    results = (
        pd
        .concat(test_results, axis=1)
        .reset_index(level=1)
        .astype(float)
        )
    results = (
        pd.concat([results], keys=['Tensile'], axis=1) # Adds tensile to multi
        .join(df[['Schedule', 'Stelmor', 'Chem', 'MTR']])
        .dropna(subset=[('Tensile', 'UT')])
        .reset_index(drop=True)
    )

    results[('Coil', 'ID')] = results[('Schedule', 'Heat')] + (
        results[('Tensile','Coil')]
        .astype(str)
        .str.replace('\.','')
        .str.replace('nan','')
        .str.pad(width=4, side='left', fillchar='0')

    )

    # Add multiindex to previous frame, combine with other sections of the data 
    # table, which do not need rearranging.
    return results

# Core function to start off downloading all of the data
def get_sqis_tensile(
        start=START, 
        end=END, 
        sub_trial_grades=True,
        table='all',
        include_chem=True,
        service='production',
        stacked=True
    ):
    '''
    grades: list of strings, or single string
    '''
    # Establish connection to database
    connection_str = connection_tensile()
    engine = create_engine(connection_str)
    connection = engine.connect()

    # Clarify whether to include the chemistry
    table = table + '_chem' if include_chem else table

    # Switch structure to select which SQL blobs need to be joined
    sql = {
        'rod': sql_rod + join_rodsize + where,
        'rod_chem': sql_rod + join_chem + join_rodsize + where,
        'rebar': sql_bar + join_rodsize + where,
        'rebar_chem': sql_bar + join_chem + join_rodsize + where,
        'all': (sql_rod + join_rodsize + where + ' UNION ' 
            + sql_bar + sql_bar + join_rodsize + where),
        'all_chem': (sql_rod + join_chem + join_rodsize + where + ' UNION '
            + sql_bar + join_chem + join_rodsize + where),
    }[table].format(
        start=start, 
        end=end, 
        chem=select_chem if include_chem else ''
        )

    #  Download. New sqlalchemy format requires encapuslting sql command as text
    df = pd.read_sql(text(sql), connection)
    # Clean up connection
    connection.close()
    # Validate if an empty table received. All kinds of untraceable errors when 
    # doing pandas manipulation occur if the frame is empty, and is hard to 
    # track down
    if len(df) == 0:
        raise ValueError('No data returned from SQL Call')
    
    # Rearrange the column names into a multiindex
    cols = df.columns.str.split('_').tolist()
    # new oracledb driver sets some columns to lower case. Not previous
    # behavior with cx_oracle
    # Only seems to affect the short abbreviations
    cols = [(x.upper() if len(x)==2 else x, y) for x, y in cols]
    df.columns = pd.MultiIndex.from_tuples(cols)

    if stacked:
        # Return tensile data in long format, not wide, no aggregates
        # Index is reset
        df = stack_tensile(df)

    # Fix 7/32, gets called many different sizes, but are functionally the same
    df.loc[
        (df['Schedule']['Size'] == '5.5mm') | 
        (df['Schedule']['Size'] == '5.5MM') |
        (df['Schedule']['Size'] == '5.5')
        , ('Schedule', 'Size')
    ] = '7/32'

    # Recalculate sizes depending on desired format
    df[('Schedule', 'Size_Dec')] = df[('Schedule', 'Size')].map(frac_to_dec, na_action='ignore')
    df[('Schedule', 'Size_Frac')] = df[('Schedule', 'Size')]
    df[('Schedule', 'Size')] = df[('Schedule', 'Size')].map(frac_to_dec_str, na_action='ignore')

    # Include predictive tensiles. A method of using chemistry to predict final tensile
    # used a linear regression
    df[('Tensile', 'PTS')] = predictive_tensile_HC9(
        pd.concat([df['Chem'], df['Schedule']['Size']], axis=1),
        size_col='Size'
    )
    df = df.drop_duplicates()
    # Include Di, another chemistry determination predicting a physical property
    df[('Chem', 'Di')] = di(df['Chem'])

    # some grades have multiple names, this unifies them
    if sub_trial_grades:
        subs = {
            'RB-14-20':'TA6763',
            'RB-15-19':'TC8560',
            'RB-15-24':'TC9438V',
            'RB-15-27':'TC6570',
            'RB-15-32':'TC6272',
            'RB-16-18':'TC8363',
            'RB-16-22':'TA9443',
            'RB-16-27':'TC2765',
            'RB-16-28':'TC8770V',
            'RB-16-38':'TC8459',
            'RB-16-43':'TC8560',
            'RB-16-44':'TC7079',
            'RB-16-45':'TC7970',
            'RB-16-46':'TC8877',
            'RB-16-48':'TA8463',
            'RB-16-51':'TC6673',
            'RB-16-61':'TC5980',
            'RB-16-63':'TC7670',
            'RB-16-67':'TC5976',
            'RB-17-02':'TC6772',
            'RB-17-03':'TC8770V',
            'RB-17-04':'TC8770',
            'RB-17-06':'TC8455',
            'RB-18-11':'TA9440',
            'RB-18-16':'TC8565',
            'RB-19-09':'TC10165',
            }
        df.replace({('Schedule', 'Grade'):subs}, inplace=True)

    return df


# Testing algorithm
if __name__ == "__main__":
    from IPython.display import display_html
    
    df = get_sqis_tensile(
        start='2021-06-01', 
        end='2021-12-31', 
        table='all')
    df[df[('Schedule', 'Heat')]=='113881']

#%%