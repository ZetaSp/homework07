cmd="""

import sqlite3 as s
conn=s.connect(':memory:')
print('[debug] Test DB connected')
q=conn.cursor()
#q.execute('drop table bank')
q.execute('create table bank(account text,password text,status text,deposit real)')
q.execute('insert into bank values("admin","passwd","active","1145.14")')
conn.commit()
print('[debug] Test data initalized.')
:newtry
tryatt=0
print()
for row in q.execute('select * from bank'):
    print('[debug] Data: '+str(row)[1:-1])

:retry
print()
usr_acc=input('Account: ')
if usr_acc=='':
    print('Have a good day!')
    print('[debug] Exiting.')
    goto('EOF')
:nopswd
usr_psw=input('Password: ')
if usr_psw=='':
    print('Please enter your password.')
    goto('nopswd')
usr_exist=0
for row in q.execute('select password,status from bank where account = "%s"'%usr_acc):
    usr_exist=1
    if usr_psw==row[0] and row[1]=='active':
        goto('success')
    elif usr_psw!=row[0] and row[1]=='active':
        tryatt+=1
        print('Incorrect account or password.')
        print(str(3-tryatt)+' attempts remaining.')
        if tryatt>=3 or tryatt<1:
            q.execute('update  bank set status = "locked" where account = "%s"'%usr_acc)
            conn.commit()
            print('Sorry, your account is locked now.')
            goto('newtry')
        else:
            goto('retry')
    elif row[1]=='locked':
        print('Account was locked.')
        goto('newtry')
    else:
        print('Unknown error.')
        goto('newtry')
    break
if usr_exist==0:
    print('Incorrect account or password.')
    goto('newtry')

:success
print()
print('='*24)
print('Welcome, '+usr_acc+'!')
print()
for row in q.execute('select deposit,status from bank where account = "%s"'%usr_acc):
    print('Deposit: USD '+str(row[0]))
    print('Status: '+row[1])
    print('='*24)
    break

#"""

while('ended'not in globals()or(str(globals().pop('inited'))[:0]
+str(globals().pop('ended'))[:0]
+str(globals().pop('re'))[:0]
+str(globals().pop('op'))[:0]
+str(globals().pop('vaddr'))[:0]
+str(globals().pop('vmemory'))[:0]
+str(globals().pop('goto'))[:0]
+str(globals().pop('gotobook'))[:0])and False):str(
    'inited'not in globals()and(
    str(    globals().update( re=__import__('re'),op=__import__('operator'),vaddr=[0],gotobook={'EOF':-1},inited=1 )   )[:0]
    +
    str(    globals().update( vmemory=
        (lambda i:
            list(map(
                lambda text:
                    (re.sub(
                        r'^:(.*)'
                        ,
                        ( lambda x:str(op.setitem(gotobook,x.group(1),i[0]) )[:0] )
                        ,
                        text
                    )+str(op.setitem(i,0,i[0]+1))[:0])
                ,
                re.split(r'\n(?! )',cmd)
            ))
        )([0])
    ,goto=lambda lable:op.setitem(vaddr,0,gotobook[lable]) )    )[:0]
    +
    str(    globals().update( gotobook={'EOF':len(vmemory)-2} )   )[:0]
    +
    str(    globals().update( vmemory=
        (lambda i:
            list(map(
                lambda text:
                    (re.sub(
                        r'^:(.*)'
                        ,
                        ( lambda x:str(op.setitem(gotobook,x.group(1),i[0]) )[:0] )
                        ,
                        text
                    )+str(op.setitem(i,0,i[0]+1))[:0])
                ,
                re.split(r'\n(?! )',cmd)
            ))
        )([0])
    ,goto=lambda lable:op.setitem(vaddr,0,gotobook[lable]) )    )[:0]
)or(
    vaddr[0]<0 or vaddr[0]>=len(vmemory)-1)and globals().update(ended=1)or(
    str(exec(vmemory[vaddr[0]]))[:0] + str(op.setitem(vaddr,0,vaddr[0]+1))[:0]
)
)[:0]or None
