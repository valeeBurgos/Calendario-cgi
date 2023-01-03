#!/usr/bin/python3

# -*- coding: utf-8 -*-
import mysql.connector
import hashlib
import sys

class DB:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

        """ 
        Hago una función que me permite obtener los datos ingresados.
        Retorna una lista de tuplas, cada tupla contiene
            (region*, comuna*, nombre_org, email_org ,celular_org, contacto_org, 
            hora_inicio, hora_termino,descripcion,tema,fotos_act) 

        """ 

    def get_comuna_id(self,comuna):
        sql = f'SELECT id FROM comuna WHERE nombre LIKE "{comuna}"' 
        self.cursor.execute(sql)
        return self.cursor.fetchall()



    #SE GUARDAN LOS DATOS
    def save_data(self, data,fotos,contacto,redes,Tema,m):
        if Tema=="ok":
            try:
                sql1 ='''
                    INSERT INTO actividad (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tema_id) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                    '''
                self.cursor.execute(sql1,data)  # ejecuta la consulta
                id_evento = self.cursor.getlastrowid()
                
                for i in fotos:
                    filename = i.filename
                    sql = "SELECT COUNT(id) FROM foto"
                    self.cursor.execute(sql)
                    total = self.cursor.fetchall()[0][0] + 1
                    filename_hash = hashlib.sha256(filename.encode()).hexdigest()[0:30] # aplica función de hash
                    filename_hash += f"_{total}"

                    open(f"media/{filename_hash}", "wb").write(i.file.read())
                    path=f"media/{filename_hash}"
                    
                    sql_file = '''
                        INSERT INTO foto (ruta_archivo, nombre_archivo, actividad_id) 
                        VALUES (%s,%s,%s);
                        '''
                    self.cursor.execute(sql_file, (path, filename_hash,id_evento))
                    self.db.commit()
                j=0
                while j<len(contacto):
                    sql3 ='''
                        INSERT INTO contactar_por (nombre, identificador, actividad_id) 
                        VALUES (%s,%s, %s);
                        '''
                    self.cursor.execute(sql3, (contacto[j],redes[j],id_evento))  # ejecuta la consulta
                    self.db.commit()                # modifico la base de datos
                    j=j+1
            except Exception as e:
                print("ERROR AL GUARDAR: ")
                print(e)
                sys.exit()

        
        else :
            try:
                sql7="""
                   INSERT INTO tema (nombre) 
                        VALUES (%s);
                """
                self.cursor.execute(sql7, [Tema]) 
                self.db.commit()
                

                sql1 ='''
                    INSERT INTO actividad (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tema_id) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                    '''
                self.cursor.execute(sql1,data)  # ejecuta la consulta
                id_evento = self.cursor.getlastrowid()
                #print(fotos.)
                
                for i in fotos:
                    filename = i.filename
                    sql = "SELECT COUNT(id) FROM foto"
                    self.cursor.execute(sql)
                    total = self.cursor.fetchall()[0][0] + 1
                    filename_hash = hashlib.sha256(filename.encode()).hexdigest()[0:30] # aplica función de hash
                    filename_hash += f"_{total}"

                    open(f"/media/{filename_hash}", "wb").write(i.file.read())
                    path=f"/media/{filename_hash}"
                    sql_file = '''
                        INSERT INTO foto (ruta_archivo, nombre_archivo, actividad_id) 
                        VALUES (%s,%s,%s);
                        '''
                    self.cursor.execute(sql_file, (path, filename_hash,id_evento))
                    self.db.commit()


                j=0
                while j<len(contacto):
                    sql3 ='''
                        INSERT INTO contactar_por (nombre, identificador, actividad_id) 
                        VALUES (%s,%s, %s);
                        '''
                    self.cursor.execute(sql3, (contacto[j],redes[j],id_evento))  # ejecuta la consulta
                    self.db.commit()                # modifico la base de datos
                    j=j+1

                

            except Exception as e:
                print("ERROR AL GUARDAR: ")
                print(e)
                sys.exit()


    

    
    #Para obtener una actividad.
    def get_actividades(self):
            sql = '''
                SELECT id, comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tema_id 
                FROM actividad ORDER BY id DESC
                '''
            self.cursor.execute(sql)
            return self.cursor.fetchall()

    def get_actividades(self):
        sql="""
        SELECT  AC.dia_hora_inicio, AC.dia_hora_termino, CO.nombre, AC.sector, TE.nombre,AC.nombre FROM actividad AC, comuna CO, tema TE WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()
   
   #Para selecccionar las ultimas 5 actividades con comuna y región.
    def get_5_actividades(self):
            sql = '''
                SELECT AC.id, CO.nombre, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre
                FROM actividad AC, comuna CO, tema TE 
                WHERE AC.comuna_id=CO.id 
                AND AC.tema_id=TE.id 
                ORDER BY id DESC LIMIT 5
                '''
            self.cursor.execute(sql)
            return self.cursor.fetchall()

    def get_foto_por_id(self,id_act):
        sql=f'SELECT id, ruta_archivo, nombre_archivo, actividad_id FROM foto WHERE actividad_id="{id_act}"'
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def get_actividades(self):
        sql="""
        SELECT  AC.dia_hora_inicio, AC.dia_hora_termino, CO.nombre, AC.sector, TE.nombre,AC.nombre, AC.id FROM actividad AC, comuna CO, tema TE WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def contador_fotos(self,id):
        sql=f'SELECT COUNT(ruta_archivo) FROM foto WHERE actividad_id= "{id}" '
        self.cursor.execute(sql)
        return self.cursor.fetchall()
        

    def get_datos_ubicacion(self,id):
        sql=f""" SELECT AC.id, CO.nombre, AC.sector, AC.comuna_id FROM actividad AC, comuna CO WHERE AC.comuna_id=CO.id AND AC.id="{id}"
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_datos_org(self,id):
        sql=f"""
        SELECT nombre, email, celular FROM actividad WHERE id="{id}"
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    
    def get_contactos(self,id):
        sql=f"""
        SELECT RED.nombre, RED.identificador, AC.id FROM actividad AC, contactar_por RED WHERE AC.id=RED.actividad_id AND AC.id="{id}"
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_info_actividad(self,id):
        sql=f"""
        SELECT  AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre FROM actividad AC, comuna CO, tema TE WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id AND AC.id="{id}"
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def get_region(self,id_comuna):
        slq=f"""
        SELECT region_id FROM comuna WHERE id="{id_comuna}"
        """
        self.cursor.execute(slq)
        return self.cursor.fetchall()


    def get_nombre_id(self,reg):
        sql=f"""
        SELECT nombre FROM region WHERE id="{reg}"
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_temas_id(self):
        sql="""
        SELECT nombre FROM tema
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def get_id_de_tema(self,nom):
        sql=f"""
        SELECT id FROM tema where nombre={nom}
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()




    def get_tema_id(self):
    
            sql= '''
                SELECT COUNT(*) FROM tema
            '''
            self.cursor.execute(sql)
            return self.cursor.fetchall()

    def get_fecha_inicio(self):
        sql='''
            SELECT dia_hora_inicio FROM actividad;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_categ(self):
        sql='''
            SELECT nombre FROM tema;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_todos_temas(self):
        sql='''
            SELECT TE.nombre FROM actividad AC,tema TE WHERE AC.tema_id=TE.id ;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def get_comunas_usadas(self):
        sql='''
            SELECT DISTINCT CO.nombre FROM actividad AC,comuna CO WHERE AC.comuna_id=CO.id ;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def get_n_fotos(self,com_id):
        sql=f'''
            SELECT COUNT(FO.id) FROM actividad AC,foto FO WHERE AC.id=FO.actividad_id and AC.comuna_id={com_id} ;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_actividades_por_comuna(self,com):
        sql=f"""
        SELECT  AC.dia_hora_inicio,TE.nombre,AC.sector, AC.id 
        FROM actividad AC, comuna CO, tema TE 
        WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id and CO.nombre='{com}'"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
  

