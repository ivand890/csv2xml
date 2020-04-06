def to_xml(df, filename=None, mode='w'):
    
    def row_to_xml(row, tab=0):
        xml = [' '*tab+'<item>']
        for i, col_name in enumerate(row.index):
            xml.append(' '*(tab+2)+'<field name="{0}">{1}</field>'.format(col_name, row.iloc[i]))
        xml.append(' '*tab+'</item>')
        return '\n'.join(xml)
    
    if len(df.index) == 1:
        res = '\n'.join(df.apply(row_to_xml, axis=1))
    else:
        res = '<data>\n'
        res = res + '\n'.join(df.apply(row_to_xml, axis=1, tab=2))
        res = res + '\n</data>'

    if filename is None:
        return res
    with open(filename, mode) as f:
        f.write(res)
