import psycopg2
import string_data
import json

class Database_worklog():
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
                database="KurniaZulda", 
                user='postgres', 
                password='    ', 
                host='127.0.0.1', 
                port= '5432'
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT version()')
        check_connection = self.cursor.fetchone()
        print(check_connection)

    def create_table(self):
        self.cursor.execute("""
                DROP TABLE IF EXISTS Produk, Kategori, Status; 
                
                CREATE TABLE Kategori (
                                    id_kategori int PRIMARY KEY,
                                    nama_kategori varchar(35));
                            
                CREATE TABLE Status (
                                    id_status int PRIMARY KEY,
                                    nama_status varchar(30));
                                    
                CREATE TABLE Produk (
                                    id_produk serial PRIMARY KEY,
                                    nama_produk text,
                                    harga int,
                                    kategori_id int,
                                    status_id int,
                                    FOREIGN KEY (kategori_id) REFERENCES Kategori (id_kategori),
                                    FOREIGN KEY (status_id) REFERENCES Status (id_status));
               """)
    
    def insert_value(self):           
        self.cursor.execute(f"""
                insert into Kategori (id_kategori, nama_kategori) values {string_data.data_kategori_str};
                insert into Status (id_status, nama_status) values {string_data.data_status_str};
                insert into Produk (nama_produk, harga, kategori_id, status_id) values {string_data.data_produk_str};                           
               """)
        
    def insert(self, nama_produk, harga, kategori_id, status_id):
        self.cursor.execute(f"""
                insert into Produk (nama_produk, harga, kategori_id, status_id) values (%s, %s, %s, %s);                           
               """, (nama_produk, harga, kategori_id, status_id))
        
    def update(self, id_produk, nama_produk, harga, kategori_id, status_id):
        self.cursor.execute(f"""
                                UPDATE Produk
                                SET nama_produk = %s, harga = $s, kategori_id = $s, status_id = $s
                                WHERE id_produk = %s;
                            """, (nama_produk, harga, kategori_id, status_id, id_produk))
    
    def select_bisa_dijual(self):
        self.cursor.execute(f"""
                                SELECT Produk.id_produk, Produk.nama_produk, Produk.harga, Status.nama_status
                                FROM Produk
                                INNER JOIN Status 
                                        ON Produk.status_id=Status.id_status
                                WHERE Status.nama_status = 'bisa dijual';            
                                """)
        result = self.cursor.fetchall()
        result = [{ "id_produk":i[0],
                    "nama_produk":i[1], 
                    "harga":i[2]} for i in result]
        result = {
            "status" : "Oke",
            "data" : result
        }
        return result
    
    def delete(self, id_produk):
        self.cursor.execute(f"""
                            DELETE FROM Produk
                            WHERE id_produk= %s;
                            """, (id_produk,))
        
    def select_status(self):
        self.cursor.execute(f"""
                                SELECT *
                                FROM Status          
                                """)
        result = self.cursor.fetchall()
        result = [{ "id_status":i[0],
                    "nama_status":i[1]} for i in result]
        result = {
            "status" : "Oke",
            "data" : result
        }
        return result
    
    def select_kategori(self):
        self.cursor.execute(f"""
                                SELECT *
                                FROM Kategori         
                                """)
        result = self.cursor.fetchall()
        result = [{ "id_kategori":i[0],
                    "nama_kategori":i[1]} for i in result]
        result = {
            "status" : "Oke",
            "data" : result
        }
        return result
              
    def closeNsave_connection(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    database = Database_worklog()
    database.create_table()
    database.insert_value()
    database.delete(6)
    print(database.select_bisa_dijual())
    # print(database.get_point("A", "Malang"))
    # print(database.get_data_from_table("projects"))
    # print(database.get_project_from_name("B")) 
    # database.closeNsave_connection()


