import csv


def open_and_parse_retailer_extract(retailer_extract_filename):
    ean_column = 15
    family_group_column = 5
    libelle_long_column = 17
    assortment_column = 23

    with open(retailer_extract_filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        _ = next(csv_reader)
        references_in_shop = [[lines[ean_column], lines[family_group_column], lines[libelle_long_column]] for lines in csv_reader if
                              "Hors assortiment" not in lines[assortment_column]]
    return references_in_shop


def open_and_parse_initialized_references(initialized_references_filename):
    ean_column = 2
    aisle_column = 1

    with open(initialized_references_filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        _ = next(csv_reader)
        initialized_references = [[lines[ean_column], lines[aisle_column]] for lines in csv_reader]
    return initialized_references


def complete_info_for_initialized_references(references_in_shop, initialized_references):
    complete_references_initialized_in_shop = []
    for reference_in_shop in references_in_shop:
        for initialized_reference in initialized_references:
            if reference_in_shop[0] == initialized_reference[0]:
                reference_in_shop.append(initialized_reference[1])
                complete_references_initialized_in_shop.append(reference_in_shop)
                break
    return complete_references_initialized_in_shop


def create_csv_with_references_to_track(missing_references, complete_references_initialized_in_shop):
    with open("data/missing_references.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        headers = ["EAN", "Libellé  Groupe de Famille", "Article Libellé Long", "aisle"]
        references_to_track = [headers]
        for missing_reference in missing_references:
            for complete_reference_initialized_in_shop in complete_references_initialized_in_shop:
                if missing_reference[1] == complete_reference_initialized_in_shop[1]:
                    aisle = complete_reference_initialized_in_shop[3]
                    missing_reference.append(aisle)
                    references_to_track.append(missing_reference)
                    break
        writer.writerows(references_to_track)


def track_missing_references():
    retailer_extract_filename = "data/retailer_extract_vLB.csv"
    initialized_references_filename = "data/references_initialized_in_shop.csv"

    all_references_in_shop = open_and_parse_retailer_extract(retailer_extract_filename)
    initialized_references = open_and_parse_initialized_references(initialized_references_filename)

    initialized_references_ids = [initialized_reference[0] for initialized_reference in initialized_references]
    complete_references_initialized_in_shop = complete_info_for_initialized_references(all_references_in_shop, initialized_references)

    missing_references = [ref for ref in all_references_in_shop if ref[0] not in initialized_references_ids]

    create_csv_with_references_to_track(missing_references, complete_references_initialized_in_shop)


if __name__ == "__main__":
    track_missing_references()
