# ExpiryApp

In order to run the script, you need to type the following line of code within the ExpiryApp repository:

```bash
python tracker.py
```

##A detailed explanation of the analysis performed.
I put csv on a data folder.
I used EAN as a product reference id.
From the retailer extract, I considered only product references without "Hors assortiment" in column "Etat Assortiment".
Among those products, I removed those that were already initialized in references_initialized_in_shop.csv.
To determine in which aisle our users should add these new products, I went through already initialized products,
and when I found one with the same "Libelle groupe de famille", I suggested the same aisle for this new product.

In the returned csv, we have only products that are not yet initialized but in the same "groupe de famille" as the ones that are already initialized.
The column we return in this csv :
- EAN,
- Libellé  Groupe de Famille,
- Article Libellé Long,
- Aisle

The csv appears in the data folder.


## A short text explaining your technical decisions and possible areas of improvement of the data analysis.
I considered that products from the same "Groupe de famille" are in the same aisle but i could have gone more deeply into "Libellé  Famille" and "Libellé sous-Famille" to be more precise on the aisle.
To be able to use this script with different csv, i could have put 2 args in command line :
- retailer_extract filename,
- references_initialized_in_shop filename.