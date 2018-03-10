items=['T-shirt','sweater']
print('our items: ',*items, sep=' ')

items.append('jeans')
print('our new items: ',*items,sep=' ')

pos=int(input('what is the position you want to update? '))

if pos<=3:

    items[pos-1]='skirt'
    print('our update new items: ',*items,sep=' ')
else:
    print('not found')

delpos=int(input('what is the position you want to delete? '))


if pos<=3:
    del items[delpos-1]
    print('our ramain items: ',*items,sep=' ')
else:
    print('not found')
