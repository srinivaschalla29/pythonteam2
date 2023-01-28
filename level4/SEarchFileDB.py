def searchDB(self,fil):
    self="filename"
    sql=""""select*from filelog where filename like '%{0}'""".format(fill)
    self.cur.execute(sql)
    row=self.cur.fetchone()
    if row==none:
        return
    else:
        return row
def insertDB(self,filename)