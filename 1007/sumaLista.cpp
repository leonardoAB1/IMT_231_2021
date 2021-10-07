int sumaLista(int laLista[], int size) {
    int suma = 0;
    int i = 0;
    while (i < size) {
        suma += laLista[i];
        i++;
    }
    return suma;
}
