```java
   long eL(long var1) {
        return var1 == 0L?145179942L:this.lC(var1 - 1L) ^ this.sy(var1 - 1L);
    }

   long lC(long var1) {
        return var1 == 0L?145179942L:this.sy(var1 - 1L) ^ this.eL(var1 - 1L);
   }

   long sy(long var1) {
        return var1 == 0L?145179942L:this.eL(var1 - 1L) ^ this.lC(var1 - 1L);
   }
```