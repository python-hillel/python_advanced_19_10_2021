from db import execute_query

s = None


def get_result(columns_list):
    sql1 = 'select {list_of_columns} from tracks limit 10;'
    result = execute_query(sql1.format(list_of_columns=columns_list))
    return result


print(get_result('TrackId, Name'))
print(get_result('TrackId, Name, AlbumId'))
