from Arvore import Arvore

a = Arvore()

a.inserir( a.raiz, 50 )
a.inserir( a.raiz, 60 )
a.inserir( a.raiz, 43 )
a.inserir( a.raiz, 5 )
a.inserir( a.raiz, 55 )

print( "\n---Em Ordem (ERD)------")
a.imprimirEmOrdem( a.raiz )
print( "\n---Pré Ordem (RED)------")
a.imprimirPreOrdem( a.raiz )
print( "\n---Pós Ordem (EDR)------")
a.imprimirPosOrdem( a.raiz )
print( "\n---Em Ordem (DRE)------")
a.imprimirReverso( a.raiz )