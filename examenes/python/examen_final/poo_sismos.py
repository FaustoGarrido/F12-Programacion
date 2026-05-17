class EventoSismico:
    def __init__(self, lugar, fecha):
        self.lugar = lugar
        self.fecha = fecha

    def clasificar(self):
        pass

    def descripcion(self):
        pass

    def __str__(self):
        return self.descripcion() or f'EventoSismico en {self.lugar}'

    def __repr__(self):
        return f'{self.__class__.__name__}(lugar={self.lugar!r}, fecha={self.fecha!r})'


class Sismo(EventoSismico):
    def __init__(self, lugar, fecha, magnitud, profundidad, tipo_escala='mww'):
        super().__init__(lugar, fecha)
        self.magnitud    = magnitud
        self.profundidad = profundidad
        self.tipo_escala = tipo_escala

    def clasificar(self):
        if self.magnitud < 6.0:
            return 'Moderado-Fuerte'
        elif self.magnitud < 7.0:
            return 'Fuerte'
        elif self.magnitud < 8.0:
            return 'Mayor'
        else:
            return 'Gran terremoto'

    def clasificar_profundidad(self):
        if self.profundidad < 70:
            return 'Superficial'
        elif self.profundidad < 300:
            return 'Intermedio'
        else:
            return 'Profundo'

    def es_peligroso(self):
        return self.magnitud >= 7.0 and self.profundidad < 70

    def descripcion(self):
        return (
            f'Sismo mag={self.magnitud:.2f} | {self.clasificar()} | '
            f'{self.clasificar_profundidad()} | Lugar: {self.lugar} | '
            f'Escala: {self.tipo_escala}'
        )

    def __str__(self):
        return self.descripcion()

    def __repr__(self):
        return (
            f'Sismo(lugar={self.lugar!r}, magnitud={self.magnitud}, '
            f'profundidad={self.profundidad}, tipo_escala={self.tipo_escala!r})'
        )


class CatalogoSismos:
    def __init__(self, nombre='Catalogo de Sismos'):
        self.nombre  = nombre
        self._sismos = []

    def agregar(self, sismo):
        self._sismos.append(sismo)

    def __len__(self):
        return len(self._sismos)

    def el_mas_intenso(self):
        if not self._sismos:
            return None
        mas_intenso = self._sismos[0]
        for sismo in self._sismos:
            if sismo.magnitud > mas_intenso.magnitud:
                mas_intenso = sismo
        return mas_intenso

    def filtrar_por_categoria(self, categoria):
        resultado = []
        for sismo in self._sismos:
            if sismo.clasificar() == categoria:
                resultado.append(sismo)
        return resultado

    def resumen(self):
        print(f'{"="*55}')
        print(f'  Catalogo : {self.nombre}')
        print(f'  Total    : {len(self)} sismos')
        print(f'  Sismo mas intenso:')
        print(f'    {self.el_mas_intenso()}')
        print(f'  Sismos por categoria:')
        for cat in ['Moderado-Fuerte', 'Fuerte', 'Mayor', 'Gran terremoto']:
            print(f'    {cat:<18}: {len(self.filtrar_por_categoria(cat))} sismos')
        print(f'{"="*55}')
