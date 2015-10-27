#include "linklist.h"
//version0.1 @Dengqi 2015-10-27
//Test by Cmake 3.21
//Implemcation of DSAAC
struct Node
{
  ElementType Element;
  Position Next;
}

int
IsEmpty(List L)
{
  return L->Next == NULL;
}


int
IsLast(Position P,List L)
{
  return P->Next == NULL;
}


Position
Find ( ElementType X , List L)
{
  Position P;
  P = L->Next;
  while( P != NULL && P->Element ! =X )
    P = P -> Next;
  return P;
}



void
Delete(ElementType X, List L)
{
  Position P, TmpCell;
  P = FindPrevious(X,L);

  if( !IsLast(X,L))
  {
    TmpCell = P->Next;
    P->Next = TmpCell->Next;
    free(TmpCell);
  }
}



Position
FindPrevious(ElementType X,List L)
{
  Position P;
  P=L;
  while( P->Next!= NULL && P->Next>Element !=x)
    p=p->Next;
  return P;
}

void
Insert(ElementType X,List L,Position P)
{
  Position TmpCell;
  //todo
  //I'm going to use java to do;
}
