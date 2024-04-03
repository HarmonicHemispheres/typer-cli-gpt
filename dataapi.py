from fastapi import FastAPI
from idsdata import *

PYTHON_API_FILE = "cats_api.py"
API = FastAPI()

@API.post("/Pull_Cats", response_model=InterjectResponse)
async def pull_cats(request: InterjectRequest):
    # Example cat data
    cats_data = IDSTable(
        TableName="Cats",
        Columns=[
            IDSColumn(ColumnName="Name", Ordinal=1),
            IDSColumn(ColumnName="Breed", Ordinal=2),
            IDSColumn(ColumnName="Quantity", Ordinal=3),
        ],
        Rows=[
            ["Whiskers", "Siamese", 5],
            ["Snowball", "Persian", 3],
            ["Mittens", "Maine Coon", 2],
            ["Socks", "Scottish Fold", 4],
            ["Boots", "Bengal", 1],
        ]
    )

    # Filter by breed if provided
    breed_param = request.get_param("breed").InputValue
    if breed_param != "":
        cats_data = cats_data.filter({"Breed": breed_param})

    # Create response
    response = InterjectResponse(
        RequestParameterList=request.RequestParameterList,
        ReturnedDataList=[
            ReturnedData(data=cats_data).to_dict(),
        ]
    )
    return response

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(API, host="127.0.0.1", port=8000)