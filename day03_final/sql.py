# Author: ray.zhang

'''
有以下员工信息表



当然此表你在文件存储时可以这样表示

1 1,Alex Li,22,13651054608,IT,2013-04-01
现需要对这个员工信息文件，实现增删改查操作

可进行模糊查询，语法至少支持下面3种:
　　select name,age from staff_table where age > 22
　　select  * from staff_table where dept = "IT"
      select  * from staff_table where enroll_date like "2013"
查到的信息，打印后，最后面还要显示查到的条数 
可创建新员工纪录，以phone做唯一键，staff_id需自增
可删除指定员工信息纪录，输入员工id，即可删除
可修改员工信息，语法如下:
　　UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
'''