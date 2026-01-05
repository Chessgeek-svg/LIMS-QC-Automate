from fastapi import FastAPI

app = FastAPI(title="OpenLIMS-QC")

@app.get("/")
def read_root():
    return {"status": "OpenLIMS-QC System Online", "version": "0.1.0"}