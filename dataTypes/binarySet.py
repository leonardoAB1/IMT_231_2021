class Set:
    def __init__(self) -> None:
        self._elements=list()
        
    def __len__(self):
        return len(self._elements)
    
    def __contains__(self, e):
        ix=self._findPosition(e)
        return ix<len(self._elements) and self._elements[ix]==e
    
    def _findPosition(self, e):
        inferior=0
        superior=len(self._elements)-1
        while inferior<=superior:
            medio=inferior+superior//2
            if self._elements[medio]==e:
                return medio
            elif e< self._elements[medio]:
                superior=medio-1
            else:
                inferiro=medio+1
        return inferior
    
    def add(self, e):
        if e not in self:
            ix=self._findPosition(e)
            self._elements.insert(ix, e)
            
    def remove(self, e):
        pass
    
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            for i in range(len(self)):
                if self._elements[i]!=setB._elements[i]:
                    return False
            return True