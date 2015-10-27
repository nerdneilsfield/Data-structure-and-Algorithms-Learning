#!/usr/bin/env python
#python3.0

print("hello world")
signed __int64 __fastcall sub_4013D0(__int64 a1, __int64 a2, __int64 a3, __int64 a4, signed int a5)
{
  __int64 v5; // rbx@1
  __int64 v6; // rax@1
  __int64 v7; // rax@9
  int v8; // ebp@12
  __int64 v9; // r14@12
  signed __int64 v10; // r13@12
  int v11; // eax@19
  signed __int64 v12; // rdx@21
  signed __int64 v13; // ST40_8@23
  int v14; // eax@24
  signed __int64 v15; // rdx@26
  __int64 v16; // rax@28
  int v17; // eax@33
  signed __int64 v18; // r13@35
  __int64 v19; // rax@38
  signed __int64 v20; // rax@40
  __int64 v21; // rdx@42
  int v22; // eax@48
  signed __int64 v23; // rbp@50
  __int64 v24; // rax@53
  signed __int64 v25; // rax@55
  __int64 v26; // rdx@57
  int v27; // eax@62
  signed __int64 v28; // rbp@64
  __int64 v29; // rax@67
  signed __int64 result; // rax@69
  __int64 v31; // rdx@70
  __int64 v32; // [sp+8h] [bp-A0h]@9
  signed __int64 v33; // [sp+10h] [bp-98h]@9
  __int64 v34; // [sp+18h] [bp-90h]@5
  __int64 v35; // [sp+20h] [bp-88h]@1
  int v36; // [sp+28h] [bp-80h]@9
  signed int v37; // [sp+38h] [bp-70h]@1
  int v38; // [sp+3Ch] [bp-6Ch]@5
  signed __int64 v39; // [sp+48h] [bp-60h]@5
  __int64 v40; // [sp+50h] [bp-58h]@1

  v5 = a4;
  v37 = a5;
  v40 = a5;
  v6 = a3;
  v35 = a3;
  while ( *(_QWORD *)(v6 + 8) || *(_QWORD *)(v6 + 16) )
  {
    if ( v37 < 0 || v37 >= *(_DWORD *)(v5 + 8) )
      goto LABEL_46;
    *(_BYTE *)(*(_QWORD *)v5 + v40) = 0;
    v34 = *(_QWORD *)(v35 + 8);
    v38 = v37 + 1;
    v39 = v40 + 1;
    while ( *(_QWORD *)(v34 + 8) || *(_QWORD *)(v34 + 16) )
    {
      if ( v38 < 0 || v38 >= *(_DWORD *)(v5 + 8) )
        goto LABEL_46;
      *(_BYTE *)(*(_QWORD *)v5 + v39) = 0;
      v36 = v38 + 1;
      v32 = *(_QWORD *)(v34 + 8);
      v7 = v32;
      v33 = v39 + 1;
      if ( !*(_QWORD *)(v32 + 8) )
        goto LABEL_32;
      do
      {
        do
        {
          if ( v36 < 0 || v36 >= *(_DWORD *)(v5 + 8) )
            goto LABEL_46;
          *(_BYTE *)(*(_QWORD *)v5 + v33) = 0;
          v8 = v36 + 1;
          v9 = *(_QWORD *)(v32 + 8);
          v10 = v33 + 1;
          while ( *(_QWORD *)(v9 + 8) || *(_QWORD *)(v9 + 16) )
          {
            if ( v8 < 0 )
              goto LABEL_46;
            if ( v8 >= *(_DWORD *)(v5 + 8) )
              goto LABEL_46;
            *(_BYTE *)(*(_QWORD *)v5 + v10) = 0;
            sub_4013D0(a1, a2, *(_QWORD *)(v9 + 8), v5, (unsigned int)(v8 + 1));
            if ( v8 >= *(_DWORD *)(v5 + 8) )
              goto LABEL_46;
            ++v8;
            *(_BYTE *)(*(_QWORD *)v5 + v10) = 1;
            v9 = *(_QWORD *)(v9 + 16);
            ++v10;
          }
          v11 = *(_DWORD *)v9;
          if ( *(_DWORD *)v9 < 0 || v11 >= *(_DWORD *)(a2 + 8) )
            goto LABEL_73;
          v12 = *(_QWORD *)a2 + 16LL * v11;
          if ( *(_DWORD *)(v12 + 8) )
            goto LABEL_74;
          if ( *(_QWORD *)v12 )
          {
            v13 = *(_QWORD *)a2 + 16LL * v11;
            operator delete[](*(void **)v12);
            v12 = v13;
          }
          *(_DWORD *)(v12 + 8) = v8;
          *(_QWORD *)v12 = operator new[](v8);
          v14 = *(_DWORD *)v9;
          if ( *(_DWORD *)v9 < 0 || v14 >= *(_DWORD *)(a2 + 8) )
            goto LABEL_73;
          v15 = *(_QWORD *)a2 + 16LL * v14;
          if ( *(_DWORD *)(v15 + 8) < v8 )
            goto LABEL_75;
          if ( v8 > 0 )
          {
            v16 = 0LL;
            do
            {
              *(_BYTE *)(*(_QWORD *)v15 + v16) = *(_BYTE *)(*(_QWORD *)v5 + v16);
              ++v16;
            }
            while ( v8 > (signed int)v16 );
          }
          if ( v36 >= *(_DWORD *)(v5 + 8) )
LABEL_46:
            __assert_fail(
              "i >= 0 && i < length",
              "huffman.cc",
              0x2Fu,
              "T& Array<T>::operator[](int) [with T = unsigned char]");
          *(_BYTE *)(*(_QWORD *)v5 + v33) = 1;
          v32 = *(_QWORD *)(v32 + 16);
          ++v33;
          ++v36;
          v7 = v32;
        }
        while ( *(_QWORD *)(v32 + 8) );
LABEL_32:
        ;
      }
      while ( *(_QWORD *)(v7 + 16) );
      v17 = *(_DWORD *)v7;
      if ( v17 < 0 || v17 >= *(_DWORD *)(a2 + 8) )
        goto LABEL_73;
      v18 = *(_QWORD *)a2 + 16LL * v17;
      if ( *(_DWORD *)(v18 + 8) )
        goto LABEL_74;
      if ( *(_QWORD *)v18 )
        operator delete[](*(void **)v18);
      *(_DWORD *)(v18 + 8) = v36;
      *(_QWORD *)v18 = operator new[](v36);
      v19 = *(_DWORD *)v32;
      if ( (signed int)v19 < 0 || (signed int)v19 >= *(_DWORD *)(a2 + 8) )
        goto LABEL_73;
      v20 = *(_QWORD *)a2 + 16 * v19;
      if ( *(_DWORD *)(v20 + 8) < v36 )
        goto LABEL_75;
      if ( v36 > 0 )
      {
        v21 = 0LL;
        do
        {
          *(_BYTE *)(*(_QWORD *)v20 + v21) = *(_BYTE *)(*(_QWORD *)v5 + v21);
          ++v21;
        }
        while ( v36 > (signed int)v21 );
      }
      if ( v38 >= *(_DWORD *)(v5 + 8) )
        goto LABEL_46;
      *(_BYTE *)(*(_QWORD *)v5 + v39) = 1;
      v34 = *(_QWORD *)(v34 + 16);
      ++v39;
      ++v38;
    }
    v22 = *(_DWORD *)v34;
    if ( *(_DWORD *)v34 < 0 || v22 >= *(_DWORD *)(a2 + 8) )
      goto LABEL_73;
    v23 = *(_QWORD *)a2 + 16LL * v22;
    if ( *(_DWORD *)(v23 + 8) )
      goto LABEL_74;
    if ( *(_QWORD *)v23 )
      operator delete[](*(void **)v23);
    *(_DWORD *)(v23 + 8) = v38;
    *(_QWORD *)v23 = operator new[](v38);
    v24 = *(_DWORD *)v34;
    if ( (signed int)v24 < 0 || (signed int)v24 >= *(_DWORD *)(a2 + 8) )
      goto LABEL_73;
    v25 = *(_QWORD *)a2 + 16 * v24;
    if ( *(_DWORD *)(v25 + 8) < v38 )
      goto LABEL_75;
    if ( v38 > 0 )
    {
      v26 = 0LL;
      do
      {
        *(_BYTE *)(*(_QWORD *)v25 + v26) = *(_BYTE *)(*(_QWORD *)v5 + v26);
        ++v26;
      }
      while ( v38 > (signed int)v26 );
    }
    if ( v37 >= *(_DWORD *)(v5 + 8) )
      goto LABEL_46;
    *(_BYTE *)(*(_QWORD *)v5 + v40) = 1;
    v35 = *(_QWORD *)(v35 + 16);
    ++v40;
    ++v37;
    v6 = v35;
  }
  v27 = *(_DWORD *)v6;
  if ( v27 < 0 || v27 >= *(_DWORD *)(a2 + 8) )
    goto LABEL_73;
  v28 = *(_QWORD *)a2 + 16LL * v27;
  if ( *(_DWORD *)(v28 + 8) )
LABEL_74:
    sub_401094();
  if ( *(_QWORD *)v28 )
    operator delete[](*(void **)v28);
  *(_DWORD *)(v28 + 8) = v37;
  *(_QWORD *)v28 = operator new[](v37);
  v29 = *(_DWORD *)v35;
  if ( (signed int)v29 < 0 || (signed int)v29 >= *(_DWORD *)(a2 + 8) )
LABEL_73:
    sub_401060();
  result = *(_QWORD *)a2 + 16 * v29;
  if ( *(_DWORD *)(result + 8) < v37 )
LABEL_75:
    __assert_fail(
      "size <= length",
      "huffman.cc",
      0x3Au,
      "void Array<T>::copy(const Array<T>&, int) [with T = unsigned char]");
  v31 = 0LL;
  if ( v37 > 0 )
  {
    do
    {
      *(_BYTE *)(*(_QWORD *)result + v31) = *(_BYTE *)(*(_QWORD *)v5 + v31);
      ++v31;
    }
    while ( v37 > (signed int)v31 );
  }
  return result;
}
