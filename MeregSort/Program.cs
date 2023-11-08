namespace MergeSort
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] A={12,2,8,5,1};
            int n=A.Length;
            Console.Write("Mang truoc khi sap xep: [");
            for (int i=0;i<n-1;i++)
            {
                Console.Write(A[i]+"; ");
            }
            Console.WriteLine(A[n-1]+"]");
            MergeSort(A,0,n-1);
            Console.Write("Mang sau khi sap xep: [");
            for (int i=0;i<n-1;i++)
            {
                Console.Write(A[i]+"; ");
            }
            Console.WriteLine(A[n-1]+"]");
        }
        private static void Merge(int[]A,int left, int mid, int right)
        {
            int i=left,k=0;
            int j=mid+1;
            int n=right-left+1;
            int[]B=new int[n];
            while((i<mid+1) & (j<right+1))
            {
                if(A[i]<A[j])
                {
                    B[k]=A[i];
                    i++;
                }
                else
                {
                    B[k]=A[j];
                    j++;
                }
                k++;
            }
            while(i<mid+1)
            {
                B[k]=A[i];
                i++;
                k++;
            }
            while(j<right+1)
            {
                B[k]=A[j];
                j++;
                k++;
            }
            i=left;
            for (k=0;k<n;k++)
            {
                A[i]=B[k];
                i++;
            }
        }
        private static void MergeSort(int[]A, int left, int right)
        {
            if (left<right)
            {
                int mid=(int) (left+right)/2;
                MergeSort(A,left,mid);
                MergeSort(A,mid+1,right);
                Merge(A,left,mid,right);
            }
        }
    }
}
