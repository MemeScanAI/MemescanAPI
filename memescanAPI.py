from fastapi import FastAPI
from memescan_api.contract_analysis import analyze_contract
from memescan_api.bundle_detection import detect_bundles
from memescan_api.trend_analysis import analyze_trends
from memescan_api.real_time_monitoring import monitor_wallet
from memescan_api.smart_chain_integration import integrate_smart_chain

# Initialize the FastAPI app
app = FastAPI()

# Define the root endpoint to check if the API is working
@app.get("/")
def read_root():
    return {"message": "Welcome to MEMESCAN API! Use /docs to explore the API endpoints."}

# Endpoint for contract analysis
@app.get("/contract_analysis/")
def contract_analysis(contract_address: str):
    """
    Analyze a Solana contract address for vulnerabilities and security risks.
    
    Parameters:
    - contract_address: The address of the Solana memecoin contract to analyze.

    Returns:
    - JSON object containing analysis results.
    """
    return analyze_contract(contract_address)

# Endpoint for bundle detection
@app.get("/bundle_detection/")
def bundle_detection(transaction_data: str):
    """
    Detect coordinated trading activities and manipulations in the memecoin market.

    Parameters:
    - transaction_data: Data about transactions to detect suspicious activities.

    Returns:
    - JSON object with detection results.
    """
    return detect_bundles(transaction_data)

# Endpoint for trend analysis
@app.get("/trend_analysis/")
def trend_analysis(market_data: str):
    """
    Predict market trends and price movements based on wallet and on-chain data.

    Parameters:
    - market_data: Data related to market sentiment and wallet activity.

    Returns:
    - JSON object with predicted market trend.
    """
    return analyze_trends(market_data)

# Endpoint for real-time wallet monitoring
@app.get("/real_time_monitoring/")
def real_time_monitoring(wallet_address: str):
    """
    Monitor a Solana wallet in real-time for suspicious activities.

    Parameters:
    - wallet_address: The address of the wallet to monitor.

    Returns:
    - JSON object with monitoring status and findings.
    """
    return monitor_wallet(wallet_address)

# Endpoint for smart chain integration
@app.get("/smart_chain_integration/")
def smart_chain_integration(contract_address: str):
    """
    Integrate with Solana's smart chain and analyze cross-contract interactions.

    Parameters:
    - contract_address: The address of the Solana memecoin contract to analyze.

    Returns:
    - JSON object with integration results.
    """
    return integrate_smart_chain(contract_address)
