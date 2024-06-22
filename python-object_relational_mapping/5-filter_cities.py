#!/usr/bin/python3
"""task 5"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    results = c.fetchall()
    cities = []
    for ct in results:
        if ct[4] == sys.argv[4]:
            cities.append(ct[2])
    city_string = ", ".join(cities)
    print(city_string)

