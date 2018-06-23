import csv
while True:
    print "1. Cluster the data using k-means.\n2. Approximate the annual rainfall for Orissa.\n3. Exit\n"
    try:
        ch=int(input("Enter choice 1,2,3: "))
    
        if ch==3:
            exit()
        """elif ch==3:
            import decisionTree
            reload(decisionTree)"""
        if ch==2:
            import multi_reg
            x=1
            while x==1:
                reload(multi_reg)
                x=int(raw_input("Continue? 1=yes,0=no"))
            
            else:
                if x!=0:
                    print 'wrong choice!'
        elif ch==1:
            import newkmeans
            
            x=1
            while x==1:
                reload(newkmeans)
                x=int(raw_input("Continue? 1=yes,0=no"))
            else:
                if x!=0:
                    print 'wrong choice!'

            
    except SyntaxError:
        print "EMPTY FIELD!"
    except NameError:
        print 'WRONG VALUE!'
    except ValueError:
        print "Enter choice as an integer number!"


