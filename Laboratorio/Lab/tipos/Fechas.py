from __future__ import annotations
from dataclasses import dataclass



@dataclass(frozen=True, order=True)

class Fecha:
    año: int
    mes: int
    dia: int 
    
    
        
    
    
    @property
    def nombre_mes(self:'Fecha')->str:
        lista_meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',\
                     'Septiembre','Octubre','Noviembre','Diciembre']
        return lista_meses[self.mes-1]




    @staticmethod
    def zeller(dia, mes,año)->str:
        if mes < 3:
            año -= 1
            mes +=12
        K = año % 100
        J = año // 100
        h=(dia + 13 * (mes +1) //5 + K + K //4 + J //4 + 5 * J) % 7
        return h
            
    @property
    def dia_semana(self:'Fecha'):
        lista_semanas=['Lunes','Martes','Miércoles','Jueves', 'Viernes','Sábado','Domingo',] 
        return lista_semanas[Fecha.zeller(self.dia,self.mes,self.mes)]
    
    
    
    
    
    @staticmethod
    def dias_en_mes (mes,año)->int:
        if mes==2:
            if (año%4==0 and año%100!=0) or (año%400==0):
                return 29 #Febrero año bisiesto
            else:
                return 28 #Feb
            
        elif mes in {4,6,9,11}: #Meses de 30 días: Abril,Junio,Septiembre,Noviembre
            return 30   
        else:
            return 31

    
                
    def sumar_dias(self, ndias) -> Fecha:
        dia = self.dia
        mes = self.mes
        año = self.año
        while ndias > 0:
            dias_en_mes = self.dias_en_mes(año, mes)
            if dia + ndias <= dias_en_mes:
                dia += ndias
                ndias = 0
            else:
                ndias -= (dias_en_mes - dia + 1)
                dia = 1
                if mes == 12:
                    mes = 1
                    año += 1
                else:
                    mes += 1
        return Fecha.of(año, mes, dia)


    
    def restar_dias(self, ndias)->Fecha:
        dia=self.dia
        mes=self.mes
        año=self.año
        while ndias > 0:
            if dia - ndias >= 1:
                dia -= ndias
                ndias = 0
            else:
                ndias -= (dia - 1)
                if mes == 1:
                    mes = 12
                    año -= 1
                else:
                    mes -= 1
                dia = Fecha.dias_en_mes(año, mes)
        return Fecha.of(año, mes, dia)
    
    
    def diferencia_en_dias(self, fecha2)->int:
        diferencia=0
        if self == fecha2:
            return 0
        elif self < fecha2:
            fecha_inicial, fecha_final = self, fecha2
        else:
            fecha_inicial, fecha_final = fecha2, self

        while fecha_inicial < fecha_final:
            fecha_inicial = fecha_inicial.sumar_dias(1)
            diferencia += 1
            dia=self.dia+1
            mes=self.mes
            año=self.año
            if dia>Fecha.dias_en_mes(año, mes):
                dia=1
                mes+=1
            if mes>12:
                mes=1
                año+=1
        if self < fecha2:
            return diferencia
        else:
            return -diferencia
        
        
        
        
        
    
    def __str__(self:'Fecha')->str:
        return f"{self.dia_semana}, {self.dia} de {self.nombre_mes} de {self.año}"
    
    @staticmethod
    def of(año, mes, dia)->Fecha:
        return Fecha(año, mes, dia)

    @staticmethod
    def parse(fecha_str)->Fecha:
        año, mes, dia = [int(part) for part in fecha_str.split('-')]
        return Fecha(año, mes, dia)
    

